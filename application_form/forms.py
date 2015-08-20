from django import forms

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

from .models import *

class SignatureForm(forms.Form):
	# pass
	signature = JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#000'}))

class AppDetailsForm(forms.ModelForm):
	POSITION_CHOICES = (
			('Position Applied', 'Position Applied'),
			('Captain', 'Captain'),
            ('Chief Mate', 'Chief Mate'),
            ('Chief Engineer', 'Chief Engineer'),
            ('2nd Engineer', '2nd Engineer'),
		)
	ALTERNATIVE_CHOICES = (
			('Alternative Position', 'Alternative Position'),
			('Captain', 'Captain'),
            ('Chief Mate', 'Chief Mate'),
            ('Chief Engineer', 'Chief Engineer'),
            ('2nd Engineer', '2nd Engineer'),
		)
	position_applied = forms.ChoiceField(choices=POSITION_CHOICES, error_messages={'invalid_choice': 'Please select a valid choice'})
	alternative_position = forms.ChoiceField(choices=ALTERNATIVE_CHOICES, error_messages={'invalid_choice': 'Please select a valid choice'})
	class Meta:
		model = AppDetails
		fields = ('application_date', 'position_applied', 'alternative_position')
		
class AppSourceForm(forms.ModelForm):
	SOURCE_CHOICES = (
			('Advertisement', 'Advertisement'),
			('Internet', 'Internet'),
			('Friends or Relatives', 'Friends or Relatives'),
			('Seafarer Center', 'Seafarer Center'),
		)
	source = forms.ChoiceField(widget=forms.RadioSelect, choices=SOURCE_CHOICES, error_messages={'required': 'Please let us know how you learned our company'})
	class Meta:
		model = AppSource
		fields = ('source', )

class PersonalDataForm(forms.ModelForm):
	age = forms.IntegerField(error_messages={'required': 'Please Fill up your Date of Birth'})
	class Meta:
		model = PersonalData
		fields = '__all__'

class PermanentAddressForm(forms.ModelForm):
	class Meta:
		model = PermanentAddress
		fields = '__all__'

class CurrentAddressForm(forms.ModelForm):
	class Meta:
		model = CurrentAddress
		fields = '__all__'

class SpouseForm(forms.ModelForm):
	class Meta:
		model = Spouse
		fields = '__all__'

class CollegeForm(forms.ModelForm):
	class Meta:
		model = College
		fields = '__all__'
		
class HighSchoolForm(forms.ModelForm):
	class Meta:
		model = HighSchool
		fields = '__all__'
		
class EmergencyContactForm(forms.ModelForm):
	class Meta:
		model = EmergencyContact
		fields = '__all__'

class BackgroundInformationForm(forms.ModelForm):
	
	class Meta:
		model = BackgroundInformation
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		CHOICES = (
			('1	', 'Yes'),
			('0', 'No'),
		)
		super(BackgroundInformationForm, self).__init__(*args, **kwargs)

		FieldList = ['visa_application', 'detained', 'disciplinary_action']
		for field in FieldList:
			self.fields[field].widget = forms.RadioSelect(choices=CHOICES)
			# Sets the booleanfield as required
			self.fields[field].required = True

# class SeaServiceForm(forms.ModelForm):
# 	class Meta:
# 		model = SeaService
		

		
# class PassportForm(forms.ModelForm):
# 	class Meta:
# 		model = Passport
		
# class SBookForm(forms.ModelForm):
# 	class Meta:
# 		model = SBook
		
# class COCForm(forms.ModelForm):
# 	class Meta:
# 		model = COC
		
# class LicenseForm(forms.ModelForm):
# 	class Meta:
# 		model = License
		
# class SRCForm(forms.ModelForm):
# 	class Meta:
# 		model = SRC
		
# class GOCForm(forms.ModelForm):
# 	class Meta:
# 		model = GOC
		
# class USVisaForm(forms.ModelForm):
# 	class Meta:
# 		model = USVisa
		
# class SchengenVisaForm(forms.ModelForm):
# 	class Meta:
# 		model = SchengenVisa
		
# class YellowFeverForm(forms.ModelForm):
# 	class Meta:
# 		model = YellowFever
		
# class CertificatesDocumentsForm(forms.ModelForm):
# 	class Meta:
# 		model = CertificatesDocuments
		
# class FlagDocumentsForm(forms.ModelForm):
# 	class Meta:
# 		model = FlagDocuments
		
# class TrainingCertificatesForm(forms.ModelForm):
# 	class Meta:
# 		model = TrainingCertificates
		
# class ReferenceForm(forms.ModelForm):
# 	class Meta:
# 		model = Reference
		
# class AppForm(forms.ModelForm):
# 	class Meta:
# 		model = AppForm

# class SignatureFormForm(forms.Form):
# 	# pass
# 	signature = JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#CCC'}))

# class SampleFormForm(forms.ModelForm):
# 	class Meta:
# 		model = Sample
# 		fields = ('name', 'picture') 