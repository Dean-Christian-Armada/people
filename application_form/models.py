from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

from django_date_extensions.fields import ApproximateDateField

from login.models import UserProfile

# Notes
#  Use ModelBase / class model inheritance for created and modified
# change user onetoone field

# START NORMALIZATION

# ManyToMany Fields for 3NFs
class Flags(models.Model):
	flags = models.CharField(max_length=50, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
class FlagDocuments(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	flags = models.ManyToManyField(Flags, blank=True, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class TrainingCertificates(models.Model):
	trainings_certificates = models.CharField(max_length=100, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
class TrainingCertificateDocuments(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	trainings_certificates = models.ManyToManyField(TrainingCertificates, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)


# Foreign Models for 2NFs
class BirthPlace(models.Model):
	birth_place = models.CharField(max_length=50, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

class VesselName(models.Model):
	vessel_name = models.CharField(max_length=50, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class VesselType(models.Model):
	vessel_type = models.CharField(max_length=50, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class Principal(models.Model):
	principal = models.CharField(max_length=50, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class CivilStatus(models.Model):
	civil_status = models.CharField(max_length=50, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

class Colleges(models.Model):
	college = models.CharField(max_length=100, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	# full_name = models.CharField(max_length=100, null=True, default=None)

class Degree(models.Model):
	degree = models.CharField(max_length=100, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	# full_name = models.CharField(max_length=100, null=True, default=None)

class HighSchools(models.Model):
	highschool = models.CharField(max_length=100, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	# full_name = models.CharField(max_length=100, null=True, default=None)

class Relationship(models.Model):
	relationship = models.CharField(max_length=50, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class Rank(models.Model):
	rank = models.CharField(max_length=50, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class EngineType(models.Model):
	engine_type = models.CharField(max_length=50, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class ManningAgency(models.Model):
	manning_agency = models.CharField(max_length=50, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class CauseOfDischarge(models.Model):
	cause_of_discharge = models.CharField(max_length=50, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class Municipality(models.Model):
	municipality = models.CharField(max_length=50, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class Barangay(models.Model):
	barangay = models.CharField(max_length=50, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class Sources(models.Model):
	source = models.CharField(max_length=50, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class Specifics(models.Model):
	specific = models.CharField(max_length=50, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class Reasons(models.Model):
	reason = models.TextField(blank=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class Status(models.Model):
	status = models.CharField(max_length=50, null=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

# Foreign Models for 1NFs

class Spouse(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	name = models.CharField(max_length=100, null=True, blank=True, default=None)
	married_date = models.DateField(null=True, blank=True, default=None)
	birthdate = models.DateField(null=True, blank=True, default=None)
	contact = models.CharField(max_length=100, null=True, blank=True, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class College(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	college = models.ForeignKey(Colleges, related_name='Colleges', default=None)
	degree = models.ForeignKey(Degree, default=None)
	schoolyear_from = models.PositiveSmallIntegerField(default=None)
	schoolyear_to = models.PositiveSmallIntegerField(default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

class HighSchool(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	highschool = models.ForeignKey(HighSchools, related_name='Highschools', default=None)
	schoolyear_from = models.PositiveSmallIntegerField(default=None)
	schoolyear_to = models.PositiveSmallIntegerField(default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

class Zip(models.Model):
	zip = models.PositiveIntegerField(default=None)
	barangay = models.ForeignKey(Barangay, default=None)
	municipality = models.ForeignKey(Municipality, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class EmergencyContact(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	relationship = models.ForeignKey(Relationship, default=None)
	zip = models.ForeignKey(Zip, default=None)
	name = models.CharField(max_length=100, null=True, default=None)
	contact = models.CharField(max_length=100, null=True, default=None)
	street = models.CharField(max_length=50, null=True, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class CurrentAddress(models.Model):
	zip = models.ForeignKey(Zip, default=None)
	street = models.CharField(max_length=50, null=True, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class PermanentAddress(models.Model):
	zip = models.ForeignKey(Zip, default=None)
	street = models.CharField(max_length=50, null=True, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class AppSource(models.Model):
	source = models.ForeignKey(Sources, default=None)
	specific = models.ForeignKey(Specifics, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

# START Background Info
class VisaApplication(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	visa_application = models.NullBooleanField(default=None)
	reason = models.ForeignKey(Reasons, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class Detained(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	detained = models.NullBooleanField(default=None)
	reason = models.ForeignKey(Reasons, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class DisciplinaryAction(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	disciplinary_action = models.NullBooleanField(default=None)
	reason = models.ForeignKey(Reasons, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
# END Background Info

class Passport(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	passport = models.CharField(max_length=100, null=True, unique=True, default=None)
	expiry = models.DateField(default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class Sbook(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	sbook = models.CharField(max_length=100, null=True, unique=True, default=None)
	expiry = models.DateField(default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class COC(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	coc = models.CharField(max_length=100, null=True, unique=True, default=None)
	expiry = models.DateField(default=None)
	rank = models.ForeignKey(Rank, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class License(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	license = models.CharField(max_length=100, null=True, unique=True, default=None)
	expiry = models.DateField(default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class SRC(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	src = models.CharField(max_length=100, null=True, unique=True, default=None)
	rank = models.ForeignKey(Rank, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class GOC(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	goc = models.CharField(max_length=100, null=True, unique=True, default=None)
	expiry = models.DateField(default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class USVisa(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	us_visa = models.CharField(max_length=100, null=True, unique=True, default=None)
	expiry = models.DateField(blank=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class SchengenVisa(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	schengen_visa = models.CharField(max_length=100, null=True, unique=True, default=None)
	expiry = models.DateField(blank=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class YellowFever(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	yellow_fever = models.CharField(max_length=100, null=True, unique=True, default=None)
	expiry = models.DateField(default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

# END NORMALIZATION


class PersonalData(models.Model):
	# Regex
	# regex for mobile numbers
	mobile_regex = RegexValidator(regex=r'^09([0-9]{9})$', message="Please input proper mobile number format 09xxxxxxxxx")
	# regex for landline numbers
	landline_regex = RegexValidator(regex=r'^([0-9]{7})$', message="Please input proper 7 digit telephone number format")
	# regex for sss
	sss_regex = RegexValidator(regex=r'^([0-9]{10})$', message="Please input proper 10 digit format of sss")
	# regex for philhealth
	philhealth_regex = RegexValidator(regex=r'^([0-9]{12})$', message="Please input proper 12 digit format of philhealth")
	# regex for tin
	tin_regex = RegexValidator(regex=r'^([0-9]{12})$', message="Please input proper 12 digit format of tin")
	# regex for pagibig
	pagibig_regex = RegexValidator(regex=r'^([0-9]{12})$', message="Please input proper 12 digit format of pagibig")
	# twelvedigit_regex = RegexValidator(regex=r'^([0-9]{12})$', message="This id contains 12 digit number") 

	# OneToOneField with Django Users Model 
	name = models.OneToOneField(UserProfile, default=None)

	# ForeignKeys
	birth_place = models.ForeignKey(BirthPlace, default=None)
	preferred_vessel_type = models.ForeignKey(VesselType, default=None)
	civil_status = models.ForeignKey(CivilStatus, default=None)
	current_address = models.ForeignKey(CurrentAddress, default=None)
	permanent_address = models.ForeignKey(PermanentAddress, default=None)

	# CharFields
	mobile_1 = models.BigIntegerField(validators=[mobile_regex], null=True, default=None)
	mobile_2 = models.BigIntegerField(validators=[mobile_regex], null=True, blank=True, default=None)
	father_name = models.CharField(max_length=100, null=True, default=None)
	mother_name = models.CharField(max_length=100, null=True, default=None)

	# Integer Fields
	age = models.PositiveIntegerField(default=None)
	landline_1 = models.PositiveIntegerField(validators=[landline_regex], null=True, blank=True, default=None)
	landline_2 = models.PositiveIntegerField(validators=[landline_regex], null=True, blank=True, default=None)
	sss = models.PositiveIntegerField(validators=[sss_regex], null=True, default=None)
	philhealth = models.BigIntegerField(validators=[philhealth_regex], null=True, blank=True, default=None)
	tin = models.BigIntegerField(validators=[tin_regex], null=True, blank=True, default=None)
	pagibig = models.BigIntegerField(validators=[pagibig_regex], null=True, blank=True, default=None)

	# EmailFields
	email_address_1 = models.EmailField(null=True, default=None)
	email_address_2 = models.EmailField(blank=True, null=True, default=None)

	# DateFields
	birth_date = models.DateField(default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

	# ThirdParty Fields
	availability_date = ApproximateDateField(default=None)


class SeaService(models.Model):

	# OneToOneField with Django Users Model 
	user = models.OneToOneField(UserProfile, default=None)

	# ForeignKeys
	vessel_name = models.ForeignKey(VesselName, default=None)
	vessel_type = models.ForeignKey(VesselType, default=None)
	flag = models.ForeignKey(Flags, default=None)
	engine_type = models.ForeignKey(EngineType, default=None)
	manning_agency = models.ForeignKey(ManningAgency, default=None)
	principal = models.ForeignKey(Principal, default=None)
	rank = models.ForeignKey(Rank, default=None)
	cause_of_discharge = models.ForeignKey(CauseOfDischarge, default=None)

	# Integer Fields
	grt = models.PositiveIntegerField(null=True, default=None)
	dwt = models.PositiveIntegerField(null=True, default=None)
	year_built = models.PositiveSmallIntegerField(null=True, default=None)
	duration = models.PositiveSmallIntegerField(null=True, default=None)

	# Decimal Fields
	hp = models.DecimalField(null=True, decimal_places=1, max_digits=10, default=None)
	kw = models.DecimalField(null=True, decimal_places=1, max_digits=10, default=None)

	# Date Fields
	date_joined = models.DateField(null=True, default=None)
	date_left = models.DateField(null=True, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)


class AppForm(models.Model):

	# OneToOneField with Django Users Model 
	user = models.OneToOneField(UserProfile, default=None)
	
	# ForeignKeys
	position_applied = models.ForeignKey(Rank, related_name="position_applied", default=None)
	alternative_position = models.ForeignKey(Rank, related_name="alternative_position", default=None)
	application_source = models.ForeignKey(AppSource, default=None)
	status = models.ForeignKey(Status, default=None)

	# Image Fields
	picture = models.ImageField(upload_to='application/pictures', blank=True, default=None)
	signatures = models.ImageField(upload_to='application/signatures', blank=True, default=None)

	# Date Fields
	application_date = models.DateField(default=None)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

	# Text Field
	essay = models.TextField(null=True, default=None)