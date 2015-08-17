from django.core.validators import RegexValidator
from django.db import models

# from jsignature.mixins import JSignatureFieldsMixin

# Create your models here.

# class JSignatureModel(JSignatureFieldsMixin):
# 	name = models.CharField(max_length=100, default=None)
# 	signatures = models.ImageField(upload_to='signatures', blank=True, default=None)


# class Sample(models.Model):
# 	picture = models.ImageField(upload_to='signatures', blank=True, default=None)
# 	name = models.CharField(max_length=100, default='dean')

# 	def __unicode__(self):
# 		return self.name

class AppDetails(models.Model):
	POSITION_CHOICES = (
			('M', 'Male'),
			('F', 'Female'),
		)
	application_date = models.DateField()
	position_applied = models.CharField(max_length=50, default=None, choices=POSITION_CHOICES)
	alternative_position = models.CharField(max_length=50, default=None, choices=POSITION_CHOICES)
	picture = models.ImageField(upload_to='application_pictures', blank=True)
	appsource = models.ForeignKey('AppSource')
	
	# def __str__(self):
	# 	return str(self.form_reference)

# class Source(models.Model):
# 	source = models.CharField(max_length=50, default=None)

# 	def __str__(self):
# 		return self.source


class AppSource(models.Model):
	source = models.CharField(max_length=50, default=None)
	specify = models.CharField(max_length=50, default=None)

	def __str__(self):
		return "%s - %s" % (self.source, self.specify)



##### START Educational Information

class Tertiary(models.Model):
	school = models.CharField(max_length=100, default=None)
	degree_obtained = models.CharField(max_length=50, default=None)
	_from = models.DateField()
	_to = models.DateField()

	def __str__(self):
		return str(self.school)

class HighSchool(models.Model):
	school = models.CharField(max_length=100, default=None)
	_from = models.DateField()
	_to = models.DateField()

	def __str__(self):
		return str(self.school)


class Education(models.Model):
	tertiary = models.ForeignKey('Tertiary')
	highschool = models.ForeignKey('HighSchool')

	def __str__(self):
		return self.tertiary

##### END Educational Information


class EmergencyContact(models.Model):
	name = models.CharField(max_length=100, default=None)
	number = models.IntegerField
	relationship = models.CharField(max_length=50, default=None)
	address = models.CharField(max_length=100, default=None)
	zip = models.IntegerField()

	def __str__(self):
		return str(self.name)

class BackgroundInformation(models.Model):
	visa_application = models.BooleanField(default=0)
	detained = models.BooleanField(default=0)
	disciplinary_action = models.BooleanField(default=0)


##### START National Certificates and Documents

class Passport(models.Model):
	passport = models.IntegerField(unique=True)
	issued = models.DateField()
	expiry = models.DateField()
	place = models.CharField(max_length=50, default=None)

	def __str__(self):
		return str(self.passport)

class SBook(models.Model):
	sbook = models.IntegerField(unique=True)
	issued = models.DateField()
	expiry = models.DateField()
	place = models.CharField(max_length=50, default=None)

	def __str__(self):
		return str(self.sbook)

class COC(models.Model):
	coc = models.IntegerField(unique=True)
	issued = models.DateField()
	expiry = models.DateField()
	rank = models.CharField(max_length=50, default=None)

	def __str__(self):
		return str(self.coc)

class License(models.Model):
	license = models.CharField(max_length=50, default=None, unique=True)
	issued = models.DateField()
	rank = models.CharField(max_length=50, default=None)

	def __str__(self):
		return str(self.license)

class SRC(models.Model):
	src = models.CharField(max_length=50, default=None, unique=True)
	issued = models.DateField()
	rank = models.CharField(max_length=50, default=None)

	def __str__(self):
		return str(self.src)

class GOC(models.Model):
	goc = models.CharField(max_length=50, default=None, unique=True)
	issued = models.DateField()
	expiry = models.DateField()

	def __str__(self):
		return str(self.goc)

class USVisa(models.Model):
	type = models.BooleanField()
	place_issued = models.CharField(max_length=50, default=None)
	expiry = models.DateField()

	def __str__(self):
		return str(self.type)

class SchengenVisa(models.Model):
	type = models.BooleanField()
	place_issued = models.CharField(max_length=50, default=None)
	expiry = models.DateField()

	def __str__(self):
		return str(self.type)

class YellowFever(models.Model):
	yellow_fever = models.IntegerField(unique=True)
	place_issued = models.CharField(max_length=50, default=None)
	issued = models.DateField()
	expiry = models.DateField()

	def __str__(self):
		return str(self.yellow_fever)

class CertificatesDocuments(models.Model):
	passport = models.ForeignKey('Passport')
	sbook = models.ForeignKey('SBook')
	coc = models.ForeignKey('COC')
	license = models.ForeignKey('License')
	src = models.ForeignKey('SRC')
	goc = models.ForeignKey('GOC')
	us_visa = models.ForeignKey('USVisa')
	schgengen_visa = models.ForeignKey('SchengenVisa')
	yellow_fever = models.ForeignKey('YellowFever')

##### END National Certificates and Documents


class FlagDocuments(models.Model):
	flags = models.CharField(max_length=100, default=None)

	def __str__(self):
		return str(self.flags)

class TrainingCertificates(models.Model):
	trainings_certificates = models.CharField(max_length=100, default=None)

	def __str__(self):
		return str(self.trainings_certificates)

class PersonalData(models.Model):
	last_name = models.CharField(max_length=50, default=None)
	first_name = models.CharField(max_length=50, default=None)
	middle_name = models.CharField(max_length=50, default=None)
	age = models.IntegerField()
	birth_date = models.DateField()
	landline_1 = models.IntegerField()
	mobile_1 = RegexValidator(regex=r'^([0-9]{11})$')
	email_address_1 = models.EmailField()
	landline_2 = models.IntegerField()
	mobile_2 = RegexValidator(regex=r'^([0-9]{11})$')
	email_address_2 = models.EmailField()
	preferred_vessel_type = models.CharField(max_length=50, default=None)
	availability_date = models.DateField()
	sss = models.IntegerField()
	philhealth = models.IntegerField()
	tin = models.IntegerField()
	pagibig = models.IntegerField()
	permanent_address = models.CharField(max_length=50, default=None)
	permanent_address_zip = models.IntegerField()
	current_address = models.CharField(max_length=50, default=None)
	current_address_zip = models.IntegerField()
	flags = models.ManyToManyField(FlagDocuments)
	training_certificates = models.ManyToManyField(TrainingCertificates)
	# sea_service = models.ForeignKey(SeaService, default=None)

	def __str__(self):
		name = "%s %s %s" % (self.first_name, self.middle_name, self.last_name, )
		return name

class Reference(models.Model):
	verified_by = models.CharField(max_length=100, null=True, blank=True, default=None)
	date = models.DateField()
	company_name = models.CharField(max_length=50, null=True, blank=True, default=None)
	person_contacted = models.CharField(max_length=100, null=True, blank=True, default=None)
	veracity_history = models.CharField(max_length=50, null=True, blank=True, default=None)
	health_problem = models.CharField(max_length=50, null=True, blank=True, default=None)
	financial_liability = models.CharField(max_length=50, null=True, blank=True, default=None)
	character = models.TextField(null=True, blank=True,)
	comments = models.TextField(null=True, blank=True,)

class AppForm(models.Model):
	# form_reference = models.CharField(max_length=50, default=None)
	app_details = models.ForeignKey('AppDetails')
	personal_data = models.ForeignKey('PersonalData')
	education = models.ForeignKey('Education')
	emergency_contact = models.ForeignKey('EmergencyContact')
	background_information = models.ForeignKey('BackgroundInformation')
	certificates_documents = models.ForeignKey('CertificatesDocuments')
	reference = models.ForeignKey('Reference', default=None)
	# sea_service = models.ForeignKey('SeaService', default=None)
	essay = models.TextField(default=None)
	signature = models.ImageField(upload_to='signatures', blank=True, default=None)

class SeaService(models.Model):
	app_form = models.ForeignKey('AppForm', default=None)
	vessel_name = models.CharField(max_length=50, default=None)
	vessel_type = models.CharField(max_length=50, default=None)
	flag = models.CharField(max_length=50, default=None)
	grt = models.IntegerField()
	year_built = models.IntegerField()
	engine_type = models.CharField(max_length=50, default=None)
	hp = models.IntegerField()
	manning_agency = models.CharField(max_length=50, default=None)
	principal = models.CharField(max_length=50, default=None)
	date_joined = models.DateField()
	date_left = models.DateField()
	duration = models.IntegerField()
	rank = models.CharField(max_length=50, default=None)
	cause_of_discharge = models.CharField(max_length=100, default=None)

	def __str__(self):
		return self.vessel_name