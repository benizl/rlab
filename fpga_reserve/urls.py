from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^backend/(?P<backend>[\w]+)/$', views.proxy, name='proxy'),
	url(r'^reserve/(?P<backend>[\w]+)/$', views.reserve, name='reserve'),
	url(r'^remove/(?P<alloc>[\w]+)/$', views.remove_res, name='remove'),
]
