from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',
	url(r'^$', views.redirect_to_reservation, name='redirect'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reserve/', include('fpga_reserve.urls', namespace='fpga_reserve')),
    url('^', include('django.contrib.auth.urls'))
)
