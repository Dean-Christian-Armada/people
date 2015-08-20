from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404


from jsignature.utils import draw_signature

from . forms import *

import os, shutil

# Create your views here.
def form(request):

	# sinature_form = SignatureForm(request.POST or None)
	appdetails_form = AppDetailsForm()
	appsource_form = AppSourceForm()
	personaldata_form = PersonalDataForm()
	permanentaddress_form = PermanentAddressForm()
	currentaddress_form = CurrentAddressForm()
	spouse_form = SpouseForm()
	college_form = CollegeForm()
	highschool_form = HighSchoolForm()
	emergencycontact_form = EmergencyContactForm()
	backgroundinfo_form = BackgroundInformationForm()
	if request.method == 'POST':
		# To make the request immutable
		request.POST = request.POST.copy()
		if request.POST['position_applied'] == 'Position Applied':
			request.POST['position_applied'] = ''
		if request.POST['alternative_position'] == 'Alternative Position':
			request.POST['alternative_position'] = ''
		if request.POST['civil_status'] == 'Civil Status':
			request.POST['civil_status'] = ''

		print request.POST

		appdetails_form = AppDetailsForm(request.POST)
		appsource_form = AppSourceForm(request.POST)
		personaldata_form = PersonalDataForm(request.POST)
		permanentaddress_form = PermanentAddressForm(request.POST)
		currentaddress_form = CurrentAddressForm(request.POST)
		spouse_form = SpouseForm(request.POST)
		college_form = CollegeForm(request.POST)
		highschool_form = HighSchoolForm(request.POST)
		emergencycontact_form = EmergencyContactForm(request.POST)
		backgroundinfo_form = BackgroundInformationForm(request.POST)
		if appdetails_form.is_valid() and appsource_form.is_valid() and personaldata_form.is_valid() and permanentaddress_form.is_valid() and currentaddress_form.is_valid() and spouse_form.is_valid() and college_form.is_valid() and highschool_form.is_valid() and emergencycontact_form.is_valid() and backgroundinfo_form.is_valid():
			pass
			# print "dean"
		else:
			# print "guinto"
			print appdetails_form.errors
			print appsource_form.errors
			print personaldata_form.errors
			print permanentaddress_form.errors
			print currentaddress_form.errors
			print spouse_form.errors
			print college_form.errors
			print highschool_form.errors
			print emergencycontact_form.errors
			print backgroundinfo_form.errors

	template = "application_form/index.html"
	context_dict = {"title": "Application Form"}
	# context_dict['signature_form'] = signature_form
	context_dict['appdetails_form'] = appdetails_form
	context_dict['appsource_form'] = appsource_form
	context_dict['personaldata_form'] = personaldata_form
	context_dict['permanentaddress_form'] = permanentaddress_form
	context_dict['currentaddress_form'] = currentaddress_form
	context_dict['spouse_form'] = spouse_form
	context_dict['college_form'] = college_form
	context_dict['highschool_form'] = highschool_form
	context_dict['emergencycontact_form'] = emergencycontact_form
	context_dict['backgroundinfo_form'] = backgroundinfo_form
	return render(request, template, context_dict)