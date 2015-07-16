from django.db import models

class Backend(models.Model):
	name = models.CharField(max_length=20)
	ip_addr = models.GenericIPAddressField()
	web_port = models.IntegerField()
	stream_port = models.IntegerField()

	def __unicode__(self):
		return self.name

class User(models.Model):
	name = models.CharField(max_length=100)
	uid = models.CharField(max_length=8)

	def __unicode__(self):
		return self.name

class Allocation(models.Model):
	backend = models.ForeignKey(Backend)
	user = models.ForeignKey(User)
	start = models.DateTimeField('Start Time')
	duration = models.DurationField()

	def __unicode__(self):
		return self.backend.name + "@" + str(self.start)

