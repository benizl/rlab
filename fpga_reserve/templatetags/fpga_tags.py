from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
	return dictionary.get(key)

@register.filter
def alloc_endtime(alloc):
	return alloc.end

@register.filter
def alloc_backend(alloc):
	return alloc.backend

@register.filter
def alloc_user(alloc):
	return alloc.user

@register.filter
def alloc_username(alloc):
	return alloc.user.name