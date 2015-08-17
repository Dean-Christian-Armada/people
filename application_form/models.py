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
			('Captain', 'Captain'),
            ('Chief Mate', 'Chief Mate'),
            ('Chief Engineer', 'Chief Engineer'),
            ('2nd Engineer', '2nd Engineer'),
		)
	application_date = models.DateField()
	position_applied = models.CharField(max_length=50, default=None, choices=POSITION_CHOICES)
	alternative_position = models.CharField(max_length=50, default=None, choices=POSITION_CHOICES)
	picture = models.ImageField(upload_to='application_pictures', blank=True)
	appsource = models.ForeignKey('AppSource')
	
	def __str__(self):
		return str(self.application_date)

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
	_from = models.IntegerField()
	_to = models.IntegerField()

	def __str__(self):
		return str(self.school)

class HighSchool(models.Model):
	school = models.CharField(max_length=100, default=None)
	_from = models.IntegerField()
	_to = models.IntegerField()

	def __str__(self):
		return str(self.school)


class Education(models.Model):
	tertiary = models.ForeignKey('Tertiary')
	highschool = models.ForeignKey('HighSchool')

	def __str__(self):
		return self.tertiary.school

##### END Educational Information


class EmergencyContact(models.Model):
	name = models.CharField(max_length=100, default=None)
	number = models.CharField(max_length=100, default=None)
	relationship = models.CharField(max_length=50, default=None)
	address = models.CharField(max_length=100, default=None)
	zip = models.IntegerField()

	def __str__(self):
		return str(self.name)

class BackgroundInformation(models.Model):
	visa_application = models.BooleanField(default=0)
	detained = models.BooleanField(default=0)
	disciplinary_action = models.BooleanField(default=0)

	def __str__(self):
		return "BackgroundInformation"


##### START National Certificates and Documents

class Passport(models.Model):
	passport = models.CharField(max_length=100, default=None, unique=True)
	expiry = models.DateField()
	place = models.CharField(max_length=50, default=None)

	def __str__(self):
		return str(self.passport)

class SBook(models.Model):
	sbook = models.CharField(max_length=100, default=None, unique=True)
	expiry = models.DateField()
	place = models.CharField(max_length=50, default=None)

	def __str__(self):
		return str(self.sbook)

class COC(models.Model):
	coc = models.CharField(max_length=100, default=None, unique=True)
	expiry = models.DateField()
	rank = models.CharField(max_length=50, default=None)

	def __str__(self):
		return str(self.coc)

class License(models.Model):
	license = models.CharField(max_length=50, default=None, unique=True)
	rank = models.CharField(max_length=50, default=None)

	def __str__(self):
		return str(self.license)

class SRC(models.Model):
	src = models.CharField(max_length=50, default=None, unique=True)
	rank = models.CharField(max_length=50, default=None)

	def __str__(self):
		return str(self.src)

class GOC(models.Model):
	goc = models.CharField(max_length=50, default=None, unique=True)
	expiry = models.DateField()

	def __str__(self):
		return str(self.goc)

class USVisa(models.Model):
	type = models.BooleanField()
	expiry = models.DateField()

	def __str__(self):
		return str(self.type)

class SchengenVisa(models.Model):
	type = models.BooleanField()
	expiry = models.DateField()

	def __str__(self):
		return str(self.type)

class YellowFever(models.Model):
	yellow_fever = models.IntegerField(unique=True)
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

	def __str__(self):
		return str(self.passport.passport)
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
	CIVIL_CHOICES = (
			('M', 'Married'),
            ('S', 'Single'),
		)
	last_name = models.CharField(max_length=50, default=None)
	first_name = models.CharField(max_length=50, default=None)
	middle_name = models.CharField(max_length=50, default=None)
	age = models.IntegerField()
	birth_date = models.DateField()
	landline_1 = models.IntegerField(blank=True, null=True)
	mobile_1 = models.CharField(max_length=50, blank=True, null=True)
	email_address_1 = models.EmailField(blank=True, null=True)
	landline_2 = models.IntegerField(default=None, blank=True, null=True)
	mobile_2 = models.CharField(max_length=50, blank=True, null=True)
	email_address_2 = models.EmailField(default=None, blank=True, null=True)
	preferred_vessel_type = models.CharField(max_length=50, default=None)
	availability_date = models.DateField()
	sss = models.CharField(max_length=50, default=None)
	philhealth = models.CharField(max_length=50, default=None)
	tin = models.CharField(max_length=50, default=None)
	pagibig = models.CharField(max_length=50, default=None)
	permanent_street = models.CharField(max_length=50, default=None)
	permanent_baranggay = models.CharField(max_length=50, default=None)
	permanent_town = models.CharField(max_length=50, default=None)
	permanent_municipality = models.CharField(max_length=50, default=None)
	permanent_zip = models.IntegerField()
	current_street = models.CharField(max_length=50, default=None)
	current_baranggay = models.CharField(max_length=50, default=None)
	current_town = models.CharField(max_length=50, default=None)
	current_municipality = models.CharField(max_length=50, default=None)
	current_zip = models.IntegerField()
	civil_status = models.CharField(max_length=50, default=None, blank=True, null=True, choices=CIVIL_CHOICES)
	spouse_name = models.CharField(max_length=100, default=None, blank=True, null=True)
	spouse_birthdate = models.DateField(default=None, blank=True, null=True)
	spouse_contact = models.CharField(max_length=100, default=None, blank=True, null=True)
	father_name = models.CharField(max_length=100, default=None, blank=True, null=True)
	mother_name = models.CharField(max_length=100, default=None, blank=True, null=True)
	married_date = models.DateField(default=None, blank=True, null=True)
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

	def __str__(self):
		return self.verified_by

class AppForm(models.Model):
	# form_reference = models.CharField(max_length=50, default=None)
	app_details = models.ForeignKey('AppDetails')
	personal_data = models.ForeignKey('PersonalData')
	education = models.ForeignKey('Education')
	emergency_contact = models.ForeignKey('EmergencyContact')
	background_information = models.ForeignKey('BackgroundInformation')
	certificates_documents = models.ForeignKey('CertificatesDocuments')
	reference = models.ForeignKey('Reference', default=None)
	flags = models.ManyToManyField(FlagDocuments)
	training_certificates = models.ManyToManyField(TrainingCertificates)
	# sea_service = models.ForeignKey('SeaService', default=None)
	essay = models.TextField(default=None)
	signature = models.ImageField(upload_to='signatures', blank=True, default=None)

	def __str__(self):
		appform = "%s %s %s : %s" % (self.personal_data.first_name, self.personal_data.middle_name, self.personal_data.last_name, self.app_details.application_date )
		return appform

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