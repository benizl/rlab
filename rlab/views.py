from django.shortcuts import redirect

def redirect_to_reservation(request):
	return redirect('reserve/')
