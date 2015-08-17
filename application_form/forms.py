from django import forms
<<<<<<< HEAD

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

from .models import *


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
		
# class AppFormForm(forms.ModelForm):
# 	class Meta:
# 		model = AppForm

# class SignatureFormForm(forms.Form):
# 	# pass
# 	signature = JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#CCC'}))

# class SampleFormForm(forms.ModelForm):
# 	class Meta:
# 		model = Sample
# 		fields = ('name', 'picture') 
=======
from .models import *

class AppDetails(forms.ModelForm):
	class Meta:
		model = AppDetails
		
class Source(forms.ModelForm):
	class Meta:
		model = Source
		
class AppSource(forms.ModelForm):
	class Meta:
		model = AppSource
		
class Tertiary(forms.ModelForm):
	class Meta:
		model = Tertiary
		
class HighSchool(forms.ModelForm):
	class Meta:
		model = HighSchool
		
class Education(forms.ModelForm):
	class Meta:
		model = Education
		
class EmergencyContact(forms.ModelForm):
	class Meta:
		model = EmergencyContact
		
class SeaService(forms.ModelForm):
	class Meta:
		model = SeaService
		
class BackgroundInformation(forms.ModelForm):
	class Meta:
		model = BackgroundInformation
		
class Passport(forms.ModelForm):
	class Meta:
		model = Passport
		
class SBook(forms.ModelForm):
	class Meta:
		model = SBook
		
class COC(forms.ModelForm):
	class Meta:
		model = COC
		
class License(forms.ModelForm):
	class Meta:
		model = License
		
class SRC(forms.ModelForm):
	class Meta:
		model = SRC
		
class GOC(forms.ModelForm):
	class Meta:
		model = GOC
		
class USVisa(forms.ModelForm):
	class Meta:
		model = USVisa
		
class SchengenVisa(forms.ModelForm):
	class Meta:
		model = SchengenVisa
		
class YellowFever(forms.ModelForm):
	class Meta:
		model = YellowFever
		
class CertificatesDocuments(forms.ModelForm):
	class Meta:
		model = CertificatesDocuments
		
class FlagDocuments(forms.ModelForm):
	class Meta:
		model = FlagDocuments
		
class TrainingCertificates(forms.ModelForm):
	class Meta:
		model = TrainingCertificates
		
class PersonalData(forms.ModelForm):
	class Meta:
		model = PersonalData
		
class Reference(forms.ModelForm):
	class Meta:
		model = Reference
		
class AppForm(forms.ModelForm):
	class Meta:
		model = AppForm
		
>>>>>>> 46f61ee250524bb4a2621397aa8f0a6b17fb49d4
