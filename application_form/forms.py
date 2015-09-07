from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.db.models import Q
from django import forms

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

from .models import *
from login.models import UserProfile, Userlevel
from mariners_profile.models import *
# All data input processes are located here
# def clean processes the insert data on the mariners profile

class ApplicantNameForm(forms.ModelForm):
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Last Name", 'data-toggle':'tooltip'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"First Name", 'data-toggle':'tooltip'}))
	middle_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Middle Name", 'data-toggle':'tooltip'}))
	
	class Meta:
		model = UserProfile
		fields = ('last_name', 'first_name', 'middle_name')

	def save(self, commit=True):
		userprofile = super(ApplicantNameForm, self).save(commit=False)
		user = User.objects.get(username='applicant')
		userlevel = Userlevel.objects.get(userlevel='applicant')
		userprofile.user = user
		userprofile.userlevel = userlevel
		userprofile.save()
		return userprofile

class PermanentAddressForm(forms.ModelForm):
	permanent_zip = forms.IntegerField()
	permanent_barangay = forms.CharField()
	permanent_municipality = forms.CharField()
	
	class Meta:
		model = ApplicationFormPermanentAddress
		fields = ('permanent_unit', 'permanent_street')

	def save(self, commit=True):
		permanent_zip = self.cleaned_data['permanent_zip']
		permanent_barangay = self.cleaned_data['permanent_barangay']
		permanent_municipality = self.cleaned_data['permanent_municipality']

		permanent_address = super(PermanentAddressForm, self).save(commit=False)
		municipality = Municipality.objects.get_or_create(municipality=permanent_municipality)
		if municipality:
			municipality = Municipality.objects.get(municipality=permanent_municipality)
		barangay = Barangay.objects.get_or_create(barangay=permanent_barangay)
		if barangay:
			barangay = Barangay.objects.get(barangay=permanent_barangay)
		try:
			zip = Zip.objects.get_or_create(zip=permanent_zip, barangay=barangay, municipality=municipality)[0]	
		except:
			zip = Zip.objects.get(zip=permanent_zip)
		permanent_address.permanent_zip = zip
		permanent_address.save()
		# Modify cleaned_data for var arguments on creating data on the Mariners Object
		self.cleaned_data['permanent_zip'] = zip
		# Remove data not on the Mariners Object fields
		self.cleaned_data.pop("permanent_municipality")
		self.cleaned_data.pop("permanent_barangay")
		value = self.cleaned_data
		PermanentAddress.objects.create(**value)
		return permanent_address


class CurrentAddressForm(forms.ModelForm):
	current_zip = forms.IntegerField()
	current_barangay = forms.CharField()
	current_municipality = forms.CharField()
	
	class Meta:
		model = ApplicationFormCurrentAddress
		fields = ('current_unit', 'current_street')

	def save(self, commit=True):
		current_zip = self.cleaned_data['current_zip']
		current_barangay = self.cleaned_data['current_barangay']
		current_municipality = self.cleaned_data['current_municipality']

		current_address = super(CurrentAddressForm, self).save(commit=False)
		municipality = Municipality.objects.get_or_create(municipality=current_municipality)
		if municipality:
			municipality = Municipality.objects.get(municipality=current_municipality)
		barangay = Barangay.objects.get_or_create(barangay=current_barangay)
		if barangay:
			barangay = Barangay.objects.get(barangay=current_barangay)
		try:
			zip = Zip.objects.get_or_create(zip=current_zip, barangay=barangay, municipality=municipality)[0]
		except:
			zip = Zip.objects.get(zip=current_zip)
		current_address.current_zip = zip
		current_address.save()
		# Modify cleaned_data for var arguments on creating data on the Mariners Object
		self.cleaned_data['current_zip'] = zip
		# Remove data not on the Mariners Object fields
		self.cleaned_data.pop("current_municipality")
		self.cleaned_data.pop("current_barangay")
		value = self.cleaned_data
		CurrentAddress.objects.create(**value)
		return current_address

class PersonalDataForm(forms.ModelForm):
	birth_place = forms.CharField()
	preferred_vessel_type = forms.CharField()
	# regex fild for mobile numbers
	mobile_1 = forms.RegexField(regex=r'^([0-9]{10})$', error_messages={'invalid': "Please input right mobile format. Example: 9171234567"})
	mobile_2 = forms.RegexField(regex=r'^([0-9]{10})$', error_messages={'invalid': "Please input right mobile format. Example: 9171234567"}, required=False)
	# regex fild for landline numbers
	landline_1 = forms.RegexField(regex=r'^([0-9]{7})$', error_messages={'invalid': "Please input proper 7 digit telephone number format"}, required=False)
	landline_2 = forms.RegexField(regex=r'^([0-9]{7})$', error_messages={'invalid': "Please input proper 7 digit telephone number format"}, required=False)
	# regex fild for sss
	sss = forms.RegexField(regex=r'^([0-9]{10})$', error_messages={'invalid': "Please input proper 10 digit format of sss"})
	# regex fild for philhealth
	philhealth = forms.RegexField(regex=r'^([0-9]{12})$', error_messages={'invalid': "Please input proper 12 digit format of philhealth"}, required=False)
	# regex fild for tin
	tin = forms.RegexField(regex=r'^([0-9]{12})$', error_messages={'invalid': "Please input proper 12 digit format of tin"}, required=False)
	# regex fild for pagibig
	pagibig = forms.RegexField(regex=r'^([0-9]{12})$', error_messages={'invalid': "Please input proper 12 digit format of pagibig"}, required=False)

 
	class Meta:
		model = ApplicationFormPersonalData
		fields = '__all__'
		exclude = ('name', 'birth_place', 'preferred_vessel_type', 'permanent_address', 'current_address')

	# def __init__(self, *args, **kwargs):
	# 	pass

	# def clean(self):
	# 	print self.cleaned_data
	# 	value = self.cleaned_data
	# 	PersonalData.objects.create(**value)

	def save(self, commit=True):
		birthplace = self.cleaned_data['birth_place']
		vessel_type = self.cleaned_data['preferred_vessel_type']

		personal_data = super(PersonalDataForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		permanent_address = ApplicationFormPermanentAddress.objects.latest('id')
		current_address = ApplicationFormCurrentAddress.objects.latest('id')
		birth_place = BirthPlace.objects.get_or_create(birth_place=birthplace)
		if birth_place:
			birth_place = BirthPlace.objects.get(birth_place=birthplace)
		preferred_vessel_type = VesselType.objects.get_or_create(vessel_type=vessel_type)
		if preferred_vessel_type:
			preferred_vessel_type = VesselType.objects.get(vessel_type=vessel_type)
		personal_data.name = userprofile
		personal_data.birth_place = birth_place
		personal_data.preferred_vessel_type = preferred_vessel_type
		personal_data.permanent_address = permanent_address
		personal_data.current_address = current_address
		personal_data.save()
		# Modify cleaned_data for var arguments on creating data on the Mariners Object
		self.cleaned_data['birth_place'] = birth_place
		self.cleaned_data['preferred_vessel_type'] = preferred_vessel_type
		permanent_address = PermanentAddress.objects.latest('id')
		current_address = CurrentAddress.objects.latest('id')
		self.cleaned_data['permanent_address'] = permanent_address
		self.cleaned_data['current_address'] = current_address
		self.cleaned_data['name'] = userprofile
		value = self.cleaned_data
		PersonalData.objects.create(**value)
		return personal_data

class SpouseForm(forms.ModelForm):
	spouse_contact = forms.RegexField(regex=r'^([0-9]{7}|[0-9]{11})$', error_messages={'invalid': "Telephone and Mobile Numbers are only allowed"}, required=False)
	class Meta:
		model = ApplicationFormSpouse
		fields = '__all__'
		exclude = ('user', )

	def save(self, commit=True):
		spouse = super(SpouseForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		spouse.user = userprofile
		spouse.save()
		self.cleaned_data['user'] = userprofile
		value = self.cleaned_data
		Spouse.objects.create(**value)

class CollegeForm(forms.ModelForm):
	college = forms.CharField()
	degree = forms.CharField()
	class Meta:
		model = ApplicationFormCollege
		fields = '__all__'
		exclude = ('user', 'college', 'degree' )

	def save(self, commit=True):
		college_name = self.cleaned_data['college']
		degree_obtained = self.cleaned_data['degree']

		college = super(CollegeForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		colleges = Colleges.objects.get_or_create(college_name=college_name)
		if colleges:
			colleges = Colleges.objects.get(college_name=college_name)
		degree = Degree.objects.get_or_create(degree=degree_obtained)
		if degree:
			degree = Degree.objects.get(degree=degree_obtained)
		college.user = userprofile
		college.college = colleges
		college.degree = degree
		college.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['college'] = colleges
		self.cleaned_data['degree'] = degree
		value = self.cleaned_data
		print value
		College.objects.create(**value)

class HighSchoolForm(forms.ModelForm):
	highschool = forms.CharField()
	class Meta:
		model = ApplicationFormHighSchool
		fields = '__all__'
		exclude = ('user', 'highschool')

	def save(self, commit=True):
		highschool_name = self.cleaned_data['highschool']
		print highschool_name
		highschool = super(HighSchoolForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		print "dean"
		highschools = HighSchools.objects.get_or_create(highschool_name=highschool_name)
		if highschools:
			highschools = HighSchools.objects.get(highschool_name=highschool_name)
		highschool.user = userprofile
		print highschools
		highschool.highschool = highschools
		highschool.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['highschool'] = highschools
		value = self.cleaned_data
		print value
		HighSchool.objects.create(**value)

class EmergencyContactForm(forms.ModelForm):
	relationship = forms.CharField()
	emergency_zip = forms.IntegerField()
	emergency_municipality = forms.CharField()
	emergency_barangay = forms.CharField()
	emergency_contact = forms.RegexField(regex=r'^([0-9]{7}|[0-9]{11})$', error_messages={'invalid': "Telephone and Mobile Numbers are only allowed"})
	class Meta:
		model = ApplicationFormEmergencyContact
		fields = '__all__'
		exclude = ('user', 'emergency_zip', 'relationship')

	def save(self, commit=True):
		emergency_zip = self.cleaned_data['emergency_zip']
		emergency_barangay = self.cleaned_data['emergency_barangay']
		emergency_municipality = self.cleaned_data['emergency_municipality']
		relationship = self.cleaned_data['relationship']

		emergency_contact = super(EmergencyContactForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		municipality = Municipality.objects.get_or_create(municipality=emergency_municipality)
		if municipality:
			municipality = Municipality.objects.get(municipality=emergency_municipality)
		barangay = Barangay.objects.get_or_create(barangay=emergency_barangay)
		if barangay:
			barangay = Barangay.objects.get(barangay=emergency_barangay)
		relationships = Relationship.objects.get_or_create(relationship=relationship)
		if relationships:
			relationships = Relationship.objects.get(relationship=relationship)
		try:
			zip = Zip.objects.get_or_create(zip=emergency_zip, barangay=barangay, municipality=municipality)[0]
		except:
			zip = Zip.objects.get(zip=current_zip)
		emergency_contact.user = userprofile
		emergency_contact.emergency_zip = zip
		emergency_contact.relationship = relationships
		emergency_contact.save()
		# Modify cleaned_data for var arguments on creating data on the Mariners Object
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['emergency_zip'] = zip
		self.cleaned_data['relationship'] = relationships
		# Remove data not on the Mariners Object fields
		self.cleaned_data.pop("emergency_municipality")
		self.cleaned_data.pop("emergency_barangay")
		value = self.cleaned_data
		EmergencyContact.objects.create(**value)
		return emergency_contact