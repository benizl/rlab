from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views.decorators.http import require_http_methods

from datetime import timedelta

from httpproxy.views import HttpProxy

from . import models

def index(request):
	backends = models.Backend.objects.all()

	user = request.user

	# Last allocation per-backend
	lallocs = {}
	for be in backends:
		ba = models.Allocation.objects.filter(backend=be,end__gte=timezone.now()).order_by('-end')

		if len(ba) > 0:
			lallocs[be] = ba[0]

	# Current allocation per-backend
	callocs = {}
	for be in backends:
		ba = models.Allocation.objects.filter(backend=be,
			start__lte=timezone.now(),
			end__gte=timezone.now()).order_by('-end')

		if len(ba) > 0:
			callocs[be] = ba[0]

	# Closest (future) allocations for this user. Should only have one anyway
	uallocs = models.Allocation.objects.filter(user=user,end__gte=timezone.now()).order_by('-end')

	context = {'backends' : backends,
		'lallocs' : lallocs,
		'callocs' : callocs,
		'user' : user,
		'uallocs' : uallocs,
		'can_reserve' : len(uallocs) == 0}

	return render(request, 'reserve/index.html', context)

def reserve(request, backend):
	be = get_object_or_404(models.Backend, pk=backend)
	user = request.user

	# Only allow one current allocation per user
	uallocs = models.Allocation.objects.filter(user=user, end__gte=timezone.now())
	if len(uallocs) > 0:
		return HttpResponseRedirect(reverse('fpga_reserve:index'))

	try:
		last_alloc = models.Allocation.objects.filter(backend=be,end__gte=timezone.now()).order_by('-end')[0]
		start_res = last_alloc.end
	except (ObjectDoesNotExist, IndexError):
		start_res = timezone.now()

	new_alloc = models.Allocation(backend=be, user=user,
		start=start_res,
		end=start_res + timedelta(minutes=30))

	new_alloc.save()

	if start_res < timezone.now():
		return HttpResponseRedirect(reverse('fpga_reserve:backend', args=(backend,)))
	else:
		return HttpResponseRedirect(reverse('fpga_reserve:index'))

def remove_res(request, alloc):
	a = get_object_or_404(models.Allocation, pk=alloc)

	# Rather than deleting, set the duration to zero so its never picked up. This keeps
	# it in the db for us to inspect later. TODO: Valid flag
	a.end = a.start
	a.save()

	return HttpResponseRedirect(reverse('fpga_reserve:index'))


def backend(request, backend):
	be = get_object_or_404(models.Backend, pk=backend)
	vid = be.stream_port
	user = request.user

	uallocs = models.Allocation.objects.filter(user=user, backend=be,
		start__lte=timezone.now(),
		end__gte=timezone.now())

	if len(uallocs) != 1:
		return HttpResponseRedirect(reverse('fpga_reserve:index'))

	# Total seconds until redirect is the time until the end of the reservation, less
	# 30 seconds. This little buffer just helps with ensuring there's no overlap between
	# students.
	td = uallocs[0].end - timezone.now()
	redirect_seconds = td.total_seconds() - 30

	return render(request, 'reserve/backend.html',
		{'backend' : backend,
		 'vid' : vid,
		 'alloc' : uallocs[0].pk,
		 'redirect_seconds' : redirect_seconds,
		 'expires' : uallocs[0].end})


@require_http_methods(["GET", "POST"])
def proxy(request, backend, url):
	be = get_object_or_404(models.Backend, pk=backend)
	user = request.user

	uallocs = models.Allocation.objects.filter(user=user, backend=be,
		start__lte=timezone.now(),
		end__gte=timezone.now())

	if len(uallocs) == 0:
		return HttpResponse("You don't have an allocation at this time")

	proxy_url = "http://" + be.ip_addr + ":" + str(be.web_port)
	print url, proxy_url
	view = HttpProxy.as_view(base_url=proxy_url, rewrite=True)
	return view(request, url)

