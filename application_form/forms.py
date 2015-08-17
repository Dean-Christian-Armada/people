from django import forms

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

from .models import *

class SignatureForm(forms.Form):
	# pass
	signature = JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#CCC'}))

class AppDetailsForm(forms.ModelForm):
	class Meta:
		model = AppDetails
		fields = ('application_date', 'position_applied', 'alternative_position')
		
# class AppSourceForm(forms.ModelForm):
# 	class Meta:
# 		model = AppSource
		
# class TertiaryForm(forms.ModelForm):
# 	class Meta:
# 		model = Tertiary
		
# class HighSchoolForm(forms.ModelForm):
# 	class Meta:
# 		model = HighSchool
		
# class EducationForm(forms.ModelForm):
# 	class Meta:
# 		model = Education
		
# class EmergencyContactForm(forms.ModelForm):
# 	class Meta:
# 		model = EmergencyContact
		
# class SeaServiceForm(forms.ModelForm):
# 	class Meta:
# 		model = SeaService
		
# class BackgroundInformationForm(forms.ModelForm):
# 	class Meta:
# 		model = BackgroundInformation
		
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
		
# class PersonalDataForm(forms.ModelForm):
# 	class Meta:
# 		model = PersonalData
		
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