# from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

from django_date_extensions.fields import ApproximateDateField

from login.models import UserProfile
from people.models import AbstractPersonalData



class BirthPlace(models.Model):
	birth_place = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )

class VesselName(models.Model):
	vessel_name = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class VesselType(models.Model):
	vessel_type = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class Principal(models.Model):
	principal = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class CivilStatus(models.Model):
	civil_status = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )

class Colleges(models.Model):
	college = models.CharField(max_length=100, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	# full_name = models.CharField(max_length=100, default=None)

class Degree(models.Model):
	degree = models.CharField(max_length=100, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	# full_name = models.CharField(max_length=100, default=None)

class HighSchools(models.Model):
	highschool = models.CharField(max_length=100, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	# full_name = models.CharField(max_length=100, default=None)

class Relationship(models.Model):
	relationship = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class Rank(models.Model):
	rank = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class EngineType(models.Model):
	engine_type = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class ManningAgency(models.Model):
	manning_agency = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class CauseOfDischarge(models.Model):
	cause_of_discharge = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class Municipality(models.Model):
	municipality = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class Barangay(models.Model):
	barangay = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class Sources(models.Model):
	source = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class Specifics(models.Model):
	specific = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class Reasons(models.Model):
	reason = models.TextField(blank=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class Status(models.Model):
	status = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class English(models.Model):
	english = models.CharField(max_length=50, default=None)

class Dialect(models.Model):
	dialect = models.CharField(max_length=50, default=None)

class Position(models.Model):
	position = models.CharField(max_length=50, default=None)

class Bank(models.Model):
	bank = models.CharField(max_length=50, default=None)

class Branch(models.Model):
	branch = models.CharField(max_length=50, default=None)

class PassportPlaceIssued(models.Model):
	place = models.CharField(max_length=50, default=None)

class SBookPlaceIssued(models.Model):
	place = models.CharField(max_length=50, default=None)

class Zip(models.Model):
	zip = models.PositiveIntegerField(default=None)
	barangay = models.ForeignKey(Barangay, default=None)
	municipality = models.ForeignKey(Municipality, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class CurrentAddress(models.Model):
	zip = models.ForeignKey(Zip, default=None)
	unit = models.CharField(max_length=50, default=None)
	street = models.CharField(max_length=50, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class PermanentAddress(models.Model):
	zip = models.ForeignKey(Zip, default=None)
	unit = models.CharField(max_length=50, default=None)
	street = models.CharField(max_length=50, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class PersonalData(AbstractPersonalData):
	# pass
	current_address = models.ForeignKey(CurrentAddress, default=None)
	permanent_address = models.ForeignKey(PermanentAddress, default=None)