from django.db import models
from django.contrib.auth.models import User

class Backend(models.Model):
	name = models.CharField(max_length=20)
	ip_addr = models.GenericIPAddressField()
	web_port = models.IntegerField()
	stream_port = models.IntegerField()
	board_type = models.CharField(max_length=40)

	def __unicode__(self):
		return self.name

class Allocation(models.Model):
	backend = models.ForeignKey(Backend)
	user = models.ForeignKey(User)
	start = models.DateTimeField('Start Time')
	end = models.DateTimeField('End Time')

	def __unicode__(self):
		return self.backend.name + "@" + str(self.start)

