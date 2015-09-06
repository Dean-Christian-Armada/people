from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.fields.related import ManyToManyField

from login.models import UserProfile
# from mariners_profile.models import BirthPlace, VesselType, CivilStatus

from django_date_extensions.fields import ApproximateDateField	

class AbstractPersonalData(models.Model):
	name = models.OneToOneField(UserProfile, default=None)

	# ForeignKeys
	birth_place = models.ForeignKey('mariners_profile.BirthPlace', default=None)
	preferred_vessel_type = models.ForeignKey('mariners_profile.VesselType', default=None)
	civil_status = models.ForeignKey('mariners_profile.CivilStatus', default=None)
	# current_address = models.ForeignKey(ApplicationFormCurrentAddress, default=None)
	# permanent_address = models.ForeignKey(ApplicationFormPermanentAddress, default=None)

	# CharFields
	mobile_1 = models.BigIntegerField(null=True, default=None)
	mobile_2 = models.BigIntegerField(null=True, blank=True, default=None)
	father_name = models.CharField(max_length=100, null=True, default=None)
	mother_name = models.CharField(max_length=100, null=True, default=None)

	# Integer Fields
	age = models.PositiveIntegerField(default=None)
	landline_1 = models.PositiveIntegerField(null=True, blank=True, default=None)
	landline_2 = models.PositiveIntegerField(null=True, blank=True, default=None)
	sss = models.PositiveIntegerField(null=True, default=None)
	philhealth = models.BigIntegerField(null=True, blank=True, default=None)
	tin = models.BigIntegerField(null=True, blank=True, default=None)
	pagibig = models.BigIntegerField(null=True, blank=True, default=None)

	# EmailFields
	email_address_1 = models.EmailField(null=True, default=None)
	email_address_2 = models.EmailField(blank=True, null=True, default=None)

	# DateFields
	birth_date = models.DateField(default=None)
	

	# ThirdParty Fields
	availability_date = ApproximateDateField(default=None)
	
	class Meta:
		abstract = True