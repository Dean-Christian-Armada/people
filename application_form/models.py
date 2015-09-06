# from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

from django_date_extensions.fields import ApproximateDateField

from login.models import UserProfile
from people.models import *
from mariners_profile.models import Zip


class ApplicationFormCurrentAddress(models.Model):
	current_zip = models.ForeignKey(Zip, default=None)
	current_unit = models.CharField(max_length=50, default=None)
	current_street = models.CharField(max_length=50, null=True, default=None)
	

class ApplicationFormPermanentAddress(models.Model):
	permanent_zip = models.ForeignKey(Zip, default=None)
	permanent_unit = models.CharField(max_length=50, default=None)
	permanent_street = models.CharField(max_length=50, null=True, default=None)

class ApplicationFormPersonalData(AbstractPersonalData):
	# pass
	current_address = models.ForeignKey(ApplicationFormCurrentAddress, default=None)
	permanent_address = models.ForeignKey(ApplicationFormPermanentAddress, default=None)


	def __unicode__(self):
		return self.sample