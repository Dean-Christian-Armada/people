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

class PermanentAddresForm(forms.ModelForm):
	permanent_zip = forms.IntegerField()
	permanent_baranggay = forms.CharField()
	permanent_municipality = forms.CharField()
	class Meta:
		model = ApplicationFormPermanentAddress
		fields = ('permanent_unit', 'permanent_street')

class CurrentAddresForm(forms.ModelForm):
	current_zip = forms.IntegerField()
	current_baranggay = forms.CharField()
	current_municipality = forms.CharField()
	class Meta:
		model = ApplicationFormCurrentAddress
		fields = ('current_unit', 'current_street')


class PersonalDataForm(forms.ModelForm):
	birth_place = forms.CharField()
	preferred_vessel_type = forms.CharField()
 
	class Meta:
		model = ApplicationFormPersonalData
		fields = '__all__'
		exclude = ('birth_place', 'preferred_vessel_type', 'civil_status', 'permanent_address', 'current_address')

	# def __init__(self, *args, **kwargs):
	# 	pass

	# def clean(self):
	# 	print self.cleaned_data
	# 	value = self.cleaned_data
	# 	PersonalData.objects.create(**value)

	def save(self, commit=True):
		personaldata = super(PersonalDataForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		personaldata.name = userprofile
		personaldata.save()
		return personaldata
