# from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

from django_date_extensions.fields import ApproximateDateField

from login.models import UserProfile
from people.models import *



class BirthPlace(models.Model):
	birth_place = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )

	def __unicode__(self):
		return self.birth_place

class VesselName(models.Model):
	vessel_name = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.vessel_name

class VesselType(models.Model):
	vessel_type = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.vessel_type

class Principal(models.Model):
	principal = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class CivilStatus(models.Model):
	civil_status = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )

	def __unicode__(self):
		return self.civil_status

class Colleges(models.Model):
	college_name = models.CharField(max_length=100, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	# full_name = models.CharField(max_length=100, default=None)

	def __unicode__(self):
		return self.college_name

class Degree(models.Model):
	degree = models.CharField(max_length=100, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	# full_name = models.CharField(max_length=100, default=None)

	def __unicode__(self):
		return self.degree

class HighSchools(models.Model):
	highschool_name = models.CharField(max_length=100, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	# full_name = models.CharField(max_length=100, default=None)

	def __unicode__(self):
		return self.highschool_name

class Relationship(models.Model):
	relationship = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.relationship

class Rank(models.Model):
	rank = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class COCRank(models.Model):
	coc_rank = models.CharField(max_length=50, default=None)
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

	def __unicode__(self):
		return self.municipality

class Barangay(models.Model):
	barangay = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.barangay

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

	def __unicode__(self):
		return self.reason

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
	bank = models.CharField(max_length=50, default=None,)

class Branch(models.Model):
	branch = models.CharField(max_length=50, default=None,)

class PassportPlaceIssued(models.Model):
	place = models.CharField(max_length=50, default=None, blank=True)

class SBookPlaceIssued(models.Model):
	place = models.CharField(max_length=50, default=None, blank=True)

class Zip(models.Model):
	zip = models.PositiveIntegerField(unique=True, default=None)
	barangay = models.ForeignKey(Barangay, default=None)
	municipality = models.ForeignKey(Municipality, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return unicode(self.zip)

class Flags(models.Model):
	flags = models.CharField(max_length=50, default=None)
	company_standard = models.NullBooleanField(max_length=50, default=False)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.flags

class CurrentAddress(models.Model):
	current_zip = models.ForeignKey(Zip, default=None)
	current_unit = models.CharField(max_length=50, default=None)
	current_street = models.CharField(max_length=50, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return "%s %s %s %s %s" % (self.current_unit, self.current_street, self.current_zip.barangay, self.current_zip.municipality, self.current_zip)

class PermanentAddress(models.Model):
	permanent_zip = models.ForeignKey(Zip, default=None)
	permanent_unit = models.CharField(max_length=50, default=None)
	permanent_street = models.CharField(max_length=50, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return "%s %s %s %s %s" % (self.permanent_unit, self.permanent_street, self.permanent_zip.barangay, self.permanent_zip.municipality, self.permanent_zip)

class PersonalData(AbstractPersonalData):
	# pass
	current_address = models.ForeignKey(CurrentAddress, default=None)
	permanent_address = models.ForeignKey(PermanentAddress, default=None)

class Spouse(AbstractSpouseData):
	pass

class College(AbstractCollege):
	pass

class HighSchool(AbstractHighSchool):
	pass

class EmergencyContact(AbstractEmergencyContact):
	pass

class VisaApplication(AbstractVisaApplication):
	pass
	
class Detained(AbstractDetained):
	pass	

class DisciplinaryAction(AbstractDisciplinaryAction):
	pass

class Passport(AbstractPassport):
	passport_place_issued = models.ForeignKey(PassportPlaceIssued, default=None, blank=True)

class Sbook(AbstractSbook):
	sbook_place_issued = models.ForeignKey(SBookPlaceIssued, default=None, blank=True)

class COC(AbstractCOC):
	coc_date_issued = models.DateField(default=None, null=True, blank=True)

class License(AbstractLicense):
	license_expiry = models.DateField(default=None, null=True, blank=True)
	license_date_issued = models.DateField(default=None, null=True, blank=True)

class SRC(AbstractSRC):
	src_expiry = models.DateField(default=None, null=True, blank=True)
	src_date_issued = models.DateField(default=None, null=True, blank=True)
	
class GOC(AbstractGOC):
	goc_date_issued = models.DateField(default=None, null=True, blank=True)

class USVisa(AbstractUSVisa):
	pass

class SchengenVisa(AbstractSchengenVisa):
	pass
class YellowFever(AbstractYellowFever):
	pass

class FlagDocuments(AbstractFlagDocuments):
	flags = models.ManyToManyField(Flags, through='mariners_profile.FlagDocumentsDetailed', blank=True, default=None)

class FlagDocumentsDetailed(models.Model):
	flags_documents = models.ForeignKey(FlagDocuments, on_delete=models.CASCADE)
	flags = models.ForeignKey(Flags, on_delete=models.CASCADE)
	sbook_number = models.PositiveIntegerField(null = True, blank=True)
	sbook_expiry = models.DateField(null=True, blank=True)
	license_number = models.PositiveIntegerField(null = True, blank=True)
	license_expiry = models.DateField(null=True, blank=True)

	def __unicode__(self):
		return "dean"