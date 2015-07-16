from django.contrib import admin

from .models import Backend, User, Allocation

admin.site.register(Backend)
admin.site.register(User)
admin.site.register(Allocation)
