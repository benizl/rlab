from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from . import models

def index(request):
	backends = models.Backend.objects.all()

	allocs = {}

	for be in backends:
		try:
			ba = models.Allocation.objects.filter(backend=be).order_by('-start')[0]
		except (ObjectDoesNotExist, IndexError):
			continue

		endtime = ba.start + ba.duration

		if endtime > timezone.now():
			allocs[be] = endtime

	return render(request, 'reserve/index.html', {'backends' : backends, 'allocs' : allocs})

def proxy(request, backend):
	be = get_list_or_404(models.Backend, name__iexact=backend)[0]
	return HttpResponse("Backend proxy to %s (%s, %d)" % (backend, be.ip_addr, be.web_port))
