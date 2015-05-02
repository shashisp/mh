from django.db import models
from django.contrib.auth.models import User

class Campaign(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	created_by = models.ForeignKey(User)

	def __unicode__(self):
		return self.title


class Milestone(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	campaign = models.ForeignKey(Campaign)

	def __unicode__(self):
		return self.title