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


# Renders manually made for horizontal selections
class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class HorizontalCheckboxRenderer(forms.CheckboxSelectMultiple.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


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
	age = forms.IntegerField(error_messages={'required': 'Please Fill up your Date of Birth'})

 
	class Meta:
		model = ApplicationFormPersonalData
		fields = '__all__'
		exclude = ('name', 'birth_place', 'preferred_vessel_type', 'permanent_address', 'current_address')

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
		College.objects.create(**value)

class HighSchoolForm(forms.ModelForm):
	highschool = forms.CharField()
	class Meta:
		model = ApplicationFormHighSchool
		fields = '__all__'
		exclude = ('user', 'highschool')

	def save(self, commit=True):
		highschool_name = self.cleaned_data['highschool']
		highschool = super(HighSchoolForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		highschools = HighSchools.objects.get_or_create(highschool_name=highschool_name)
		if highschools:
			highschools = HighSchools.objects.get(highschool_name=highschool_name)
		highschool.user = userprofile
		highschool.highschool = highschools
		highschool.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['highschool'] = highschools
		value = self.cleaned_data
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

class VisaApplicationForm(forms.ModelForm):
	CHOICES = (
			('1', 'Yes'),
			('0', 'No'),
		)
	visa_application = forms.NullBooleanField(widget=forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer))
	visa_application_reason = forms.CharField(required=False)
	class Meta:
		model = ApplicationFormVisaApplication
		fields = ('visa_application', )

	def clean(self):
		msg = "Please choose either yes or no"
		try:
			visa_application = selfdata['visa_application']
		except:
			visa_application = self.cleaned_data['visa_application']
		if visa_application is None:	
			self.add_error('visa_application', msg)

	def save(self, commit=True):
		reason = self.cleaned_data['visa_application_reason']
		visa_application = super(VisaApplicationForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		visa_application.user = userprofile
		reasons = Reasons.objects.get_or_create(reason=reason)
		if reasons:
			reasons = Reasons.objects.get(reason=reason)
		visa_application.visa_application_reason = reasons
		visa_application.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['visa_application_reason'] = reasons
		value = self.cleaned_data
		VisaApplication.objects.create(**value)

class DetainedForm(forms.ModelForm):
	CHOICES = (
			('1', 'Yes'),
			('0', 'No'),
		)
	detained = forms.NullBooleanField(widget=forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer))
	detained_reason = forms.CharField(required=False)
	class Meta:
		model = ApplicationFormDetained
		fields = ('detained', )

	def clean(self):
		msg = "Please choose either yes or no"
		try:
			detained = selfdata['detained']
		except:
			detained = self.cleaned_data['detained']
		if detained is None:	
			self.add_error('detained', msg)

	def save(self, commit=True):
		reason = self.cleaned_data['detained_reason']
		detained = super(DetainedForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		detained.user = userprofile
		reasons = Reasons.objects.get_or_create(reason=reason)
		if reasons:
			reasons = Reasons.objects.get(reason=reason)
		detained.detained_reason = reasons
		detained.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['detained_reason'] = reasons
		value = self.cleaned_data
		Detained.objects.create(**value)

class DisciplinaryActionForm(forms.ModelForm):
	CHOICES = (
			('1', 'Yes'),
			('0', 'No'),
		)
	disciplinary_action = forms.NullBooleanField(widget=forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer))
	disciplinary_action_reason = forms.CharField(required=False)
	class Meta:
		model = ApplicationFormDisciplinaryAction
		fields = ('disciplinary_action', )

	def clean(self):
		msg = "Please choose either yes or no"
		try:
			disciplinary_action = selfdata['disciplinary_action']
		except:
			disciplinary_action = self.cleaned_data['disciplinary_action']
		if disciplinary_action is None:	
			self.add_error('disciplinary_action', msg)

	def save(self, commit=True):
		reason = self.cleaned_data['disciplinary_action_reason']
		disciplinary_action = super(DisciplinaryActionForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		disciplinary_action.user = userprofile
		reasons = Reasons.objects.get_or_create(reason=reason)
		if reasons:
			reasons = Reasons.objects.get(reason=reason)
		disciplinary_action.disciplinary_action_reason = reasons
		disciplinary_action.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['disciplinary_action_reason'] = reasons
		value = self.cleaned_data
		DisciplinaryAction.objects.create(**value)

class PassportForm(forms.ModelForm):
	class Meta:
		model = ApplicationFormPassport
		fields = ('passport', 'passport_expiry')

	def save(self, commit=True):
		passport = super(PassportForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		passport.user = userprofile
		passport.save()
		place_issued = PassportPlaceIssued.objects.get_or_create(place='')
		if place_issued:
			place_issued = PassportPlaceIssued.objects.get(place='')
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['passport_place_issued'] = place_issued
		value = self.cleaned_data
		Passport.objects.create(**value)

class SbookForm(forms.ModelForm):
	class Meta:
		model = ApplicationFormSbook
		fields = ('sbook', 'sbook_expiry')

	def save(self, commit=True):
		sbook = super(SbookForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		sbook.user = userprofile
		sbook.save()
		place_issued = SBookPlaceIssued.objects.get_or_create(place='')
		if place_issued:
			place_issued = SBookPlaceIssued.objects.get(place='')
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['sbook_place_issued'] = place_issued
		value = self.cleaned_data
		Sbook.objects.create(**value)

class COCForm(forms.ModelForm):
	coc_rank = forms.CharField()
	class Meta:
		model = ApplicationFormCOC
		fields = ('coc', 'coc_expiry')

	def save(self, commit=True):
		rank = self.cleaned_data['coc_rank']
		coc = super(COCForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		coc.user = userprofile
		coc_rank = COCRank.objects.get_or_create(coc_rank=rank)
		if coc_rank:
			coc_rank = COCRank.objects.get(coc_rank=rank)
		coc.coc_rank = coc_rank
		coc.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['coc_rank'] = coc_rank
		self.cleaned_data['coc_date_issued'] = None
		value = self.cleaned_data
		COC.objects.create(**value)

class LicenseForm(forms.ModelForm):
	license_rank = forms.CharField()
	class Meta:
		model = ApplicationFormLicense
		fields = ('license', )

	def save(self, commit=True):
		rank = self.cleaned_data['license_rank']
		license = super(LicenseForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		license.user = userprofile
		license_rank = Rank.objects.get_or_create(rank=rank)
		if license_rank:
			license_rank = Rank.objects.get(rank=rank)
		license.license_rank = license_rank
		license.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['license_rank'] = license_rank
		self.cleaned_data['license_expiry'] = None
		self.cleaned_data['license_date_issued'] = None
		value = self.cleaned_data
		License.objects.create(**value)

class SRCForm(forms.ModelForm):
	src_rank = forms.CharField()
	class Meta:
		model = ApplicationFormSRC
		fields = ('src', )

	def save(self, commit=True):
		rank = self.cleaned_data['src_rank']
		src = super(SRCForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		src.user = userprofile
		src_rank = Rank.objects.get_or_create(rank=rank)
		if src_rank:
			src_rank = Rank.objects.get(rank=rank)
		src.src_rank = src_rank
		src.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['src_rank'] = src_rank
		self.cleaned_data['src_expiry'] = None
		self.cleaned_data['src_date_issued'] = None
		value = self.cleaned_data
		SRC.objects.create(**value)

class GOCForm(forms.ModelForm):
	class Meta:
		model = ApplicationFormGOC
		fields = ('goc', 'goc_expiry')

	def save(self, commit=True):
		goc = super(GOCForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		goc.user = userprofile
		goc.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['goc_date_issued'] = None
		value = self.cleaned_data
		GOC.objects.create(**value)

class USVisaForm(forms.ModelForm):
	CHOICES = (
			('1', 'Yes'),
			('0', 'No'),
		)
	us_visa = forms.NullBooleanField(widget=forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer))
	class Meta:
		model = ApplicationFormUSVisa
		fields = ('us_visa', 'us_visa_expiry')

	def clean(self):
		try:
			value = selfdata['us_visa']
			expiry = selfdata['us_visa_expiry']
		except:
			value = self.cleaned_data['us_visa']
			expiry = self.cleaned_data['us_visa_expiry']
		if value is None:	
			msg = "Please choose either yes or no"
			self.add_error('us_visa', msg)
		elif value == 1 and expiry is None:
			msg_expiry = "Please fill up the date of expiry"
			self.add_error('us_visa_expiry', msg_expiry)

	def save(self, commit=True):
		us_visa = super(USVisaForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		us_visa.user = userprofile
		us_visa.save()
		self.cleaned_data['user'] = userprofile
		value = self.cleaned_data
		USVisa.objects.create(**value)

class SchengenVisaForm(forms.ModelForm):
	CHOICES = (
			('1', 'Yes'),
			('0', 'No'),
		)
	schengen_visa = forms.NullBooleanField(widget=forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer))
	class Meta:
		model = ApplicationFormSchengenVisa
		fields = ('schengen_visa', 'schengen_visa_expiry')

	def clean(self):
		try:
			value = selfdata['schengen_visa']
			expiry = selfdata['schengen_visa_expiry']
		except:
			value = self.cleaned_data['schengen_visa']
			expiry = self.cleaned_data['schengen_visa_expiry']
		if value is None:	
			msg = "Please choose either yes or no"
			self.add_error('schengen_visa', msg)
		elif value == 1 and expiry is None:
			msg_expiry = "Please fill up the date of expiry"
			self.add_error('schengen_visa_expiry', msg_expiry)

	def save(self, commit=True):
		schengen_visa = super(SchengenVisaForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		schengen_visa.user = userprofile
		schengen_visa.save()
		self.cleaned_data['user'] = userprofile
		value = self.cleaned_data
		SchengenVisa.objects.create(**value)

class YellowFeverForm(forms.ModelForm):
	class Meta:
		model = ApplicationFormYellowFever
		fields = ('yellow_fever', 'yellow_fever_expiry')

	def save(self, commit=True):
		yellow_fever = super(YellowFeverForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		yellow_fever.user = userprofile
		yellow_fever.save()
		self.cleaned_data['user'] = userprofile
		value = self.cleaned_data
		YellowFever.objects.create(**value)

class FlagForm(forms.ModelForm):
	flags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(renderer=HorizontalCheckboxRenderer), queryset=Flags.objects.filter(company_standard=1), required=False)
	class Meta:
		model = ApplicationFormFlagDocuments
		fields = ('flags', )

	def save(self, commit=True):
		print self.cleaned_data
		flag = super(FlagForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		flag.user = userprofile
		flag.save()
		self.cleaned_data['user'] = userprofile
		value = self.cleaned_data
		# flagdocuments = FlagDocuments.object.get_or_create(user=user)


	def save_m2m(self, commit=True):
		print "dean"