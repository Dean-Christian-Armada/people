from django import forms
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
		
