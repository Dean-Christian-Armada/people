from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Userlevel(models.Model):
	userlevel = models.CharField(max_length=50, null=True)
	def __unicode__(self):
		return self.userlevel

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	userlevel = models.ForeignKey('Userlevel')
	phrase = models.CharField(max_length=50)

	def __unicode__(self):
		return self.user.username