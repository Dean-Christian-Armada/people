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
	mobile_1 = models.PositiveIntegerField(null=True, default=None)
	mobile_2 = models.PositiveIntegerField(null=True, blank=True, default=None)
	father_first_name = models.CharField(max_length=50, null=True, default=None)
	father_middle_name = models.CharField(max_length=50, null=True, default=None)
	father_last_name = models.CharField(max_length=50, null=True, default=None)
	mother_first_name = models.CharField(max_length=50, null=True, default=None)
	mother_middle_name = models.CharField(max_length=50, null=True, default=None)
	mother_last_name = models.CharField(max_length=50, null=True, default=None)

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

	def __unicode__(self):
		return "%s %s %s" % (self.name.first_name, self.name.middle_name, self.name.last_name)

	def save(self, *args, **kwargs):
		if self.landline_2 == '':
			self.landline_2 = None
		if self.philhealth == '':
			self.philhealth = None
		if self.tin == '':
			self.tin = None
		if self.pagibig == '':
			self.pagibig = None
		if self.landline_1 == '':
			self.landline_1 = None
		if self.mobile_2 == '':
			self.mobile_2 = None

		super(AbstractPersonalData, self).save(*args, **kwargs)
		

class AbstractSpouseData(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	spouse_first_name = models.CharField(max_length=50, null=True, blank=True, default=None)
	spouse_middle_name = models.CharField(max_length=50, null=True, blank=True, default=None)
	spouse_last_name = models.CharField(max_length=50, null=True, blank=True, default=None)
	married_date = models.DateField(null=True, blank=True, default=None)
	birthdate = models.DateField(null=True, blank=True, default=None)
	spouse_contact = models.BigIntegerField(null=True, blank=True, default=None)

	class Meta:
		abstract = True

	def save(self, *args, **kwargs):
		if self.spouse_last_name == '':
			return False
		if self.spouse_contact == '':
			self.spouse_contact = None
		super(AbstractSpouseData, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s %s" % (self.spouse_first_name, self.spouse_middle_name, self.spouse_last_name)

class AbstractCollege(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	college = models.ForeignKey('mariners_profile.Colleges', default=None)
	degree = models.ForeignKey('mariners_profile.Degree', default=None)
	collegeyear_from = models.PositiveSmallIntegerField(default=None)
	collegeyear_to = models.PositiveSmallIntegerField(default=None)

	class Meta:
		abstract = True
	
	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s - %s / %s-%s" % (user, self.college, self.collegeyear_from, self.collegeyear_to)

class AbstractHighSchool(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	highschool = models.ForeignKey('mariners_profile.HighSchools', default=None)
	schoolyear_from = models.PositiveSmallIntegerField(default=None)
	schoolyear_to = models.PositiveSmallIntegerField(default=None)

	class Meta:
		abstract = True

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s - %s / %s-%s" % (user, self.highschool, self.schoolyear_from, self.schoolyear_to)

class AbstractEmergencyContact(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	relationship = models.ForeignKey('mariners_profile.Relationship', default=None)
	emergency_zip = models.ForeignKey('mariners_profile.Zip', default=None)
	emergency_first_name = models.CharField(max_length=50, null=True, default=None)
	emergency_middle_name = models.CharField(max_length=50, null=True, default=None)
	emergency_last_name = models.CharField(max_length=50, null=True, default=None)
	emergency_contact = models.CharField(max_length=100, null=True, default=None)
	emergency_street = models.CharField(max_length=50, null=True, default=None)
	emergency_unit = models.CharField(max_length=50, null=True, default=None)

	class Meta:
		abstract = True

	def __unicode__(self):
		user = "%s %s %s" % (self.emergency_first_name, self.emergency_middle_name, self.emergency_last_name)
		return user