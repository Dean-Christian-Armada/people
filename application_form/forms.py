from django.utils.safestring import mark_safe
from django import forms

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

from .models import *

class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class HorizontalCheckboxRenderer(forms.CheckboxSelectMultiple.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

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
			self.fields[field].widget = forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer)
			# Sets the booleanfield as required
			self.fields[field].required = True

class PassportForm(forms.ModelForm):
	class Meta:
		model = Passport
		fields = ('passport', 'expiry')
		
class SBookForm(forms.ModelForm):
	class Meta:
		model = SBook
		fields = ('sbook', 'expiry')
		
class COCForm(forms.ModelForm):
	class Meta:
		model = COC
		fields = ('coc', 'expiry', 'rank')
		
class LicenseForm(forms.ModelForm):
	class Meta:
		model = License
		fields = ('license', 'rank')
		
class SRCForm(forms.ModelForm):
	class Meta:
		model = SRC
		fields = ('src', 'rank')
		
class GOCForm(forms.ModelForm):
	class Meta:
		model = GOC
		fields = ('goc', 'expiry')
		
class USVisaForm(forms.ModelForm):
	class Meta:
		model = USVisa
		fields = ('type', 'expiry')

	def __init__(self, *args, **kwargs):
		CHOICES = (
			('1	', 'Yes'),
			('0', 'No'),
		)
		super(USVisaForm, self).__init__(*args, **kwargs)

		self.fields['type'].widget = forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer)
		# Sets the booleanfield as required
		self.fields['type'].required = True
		
class SchengenVisaForm(forms.ModelForm):
	class Meta:
		model = SchengenVisa
		fields = ('type', 'expiry')

	def __init__(self, *args, **kwargs):
		CHOICES = (
			('1	', 'Yes'),
			('0', 'No'),
		)
		super(SchengenVisaForm, self).__init__(*args, **kwargs)

		self.fields['type'].widget = forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer)
		# Sets the booleanfield as required
		self.fields['type'].required = True
		
class YellowFeverForm(forms.ModelForm):
	class Meta:
		model = YellowFever
		fields = ('yellow_fever', 'expiry')

# class FlagDocumentsForm(forms.ModelForm):
# 	flags = forms.ModelMultipleChoiceField(queryset=)
# 	class Meta:
# 		model = FlagDocuments

class AppForm(forms.ModelForm):
	signature = JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#000'}), error_messages={'required': 'Please do not forget to sign before submitting'})
	flags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(renderer=HorizontalCheckboxRenderer), queryset=FlagDocuments.objects.all(), error_messages={'required': 'Please do not forget to select among the flags'})
	training_certificates = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(renderer=HorizontalCheckboxRenderer), queryset=TrainingCertificates.objects.all(), error_messages={'required': 'Please do not forget to select among the trainings and certificates'})
	class Meta:
		model = AppForm
		fields = ('essay', 'signature')

# class SignatureFormForm(forms.Form):
# 	# pass
# 	signature = JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#CCC'}))



# class SeaServiceForm(forms.ModelForm):
# 	class Meta:
# 		model = SeaService
		
# class CertificatesDocumentsForm(forms.ModelForm):
# 	class Meta:
# 		model = CertificatesDocuments
		

		
# class TrainingCertificatesForm(forms.ModelForm):
# 	class Meta:
# 		model = TrainingCertificates
		
# class ReferenceForm(forms.ModelForm):
# 	class Meta:
# 		model = Reference
		


# class SampleFormForm(forms.ModelForm):
# 	class Meta:
# 		model = Sample
# 		fields = ('name', 'picture') 