from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.forms.formsets import formset_factory
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from jsignature.utils import draw_signature

from . forms import *

import os, shutil, datetime

# Create your views here.

@login_required()
def form(request):

	# signature_form = SignatureForm(request.POST or None)
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
	passport_form = PassportForm()
	sbook_form = SBookForm()
	coc_form = COCForm()
	license_form = LicenseForm()
	src_form = SRCForm()
	goc_form = GOCForm()
	usvisa_form = USVisaForm()
	schengenvisa_form = SchengenVisaForm()
	yellowfever_form = YellowFeverForm()
	seaservice_form = formset_factory(SeaServiceForm, extra=5)
	app_form = AppForm()

	# Gets Date Today
	# today = datetime.date.today()
	# Changes format to Day/Month/Year
	# today = today.strftime("%d/%m/%y")

	if request.method == 'POST':
		# To make the request immutable
		request.POST = request.POST.copy()
		if request.POST['position_applied'] == 'Position Applied':
			request.POST['position_applied'] = ''
		if request.POST['alternative_position'] == 'Alternative Position':
			request.POST['alternative_position'] = ''
		if request.POST['civil_status'] == 'Civil Status':
			request.POST['civil_status'] = ''
		# if request.POST['cause_of_discharge'] == 'Cause of Discharge':
		# 	request.POST['cause_of_discharge'] = ''
		# flags = request.POST.get('flags', False)
		# if not flags:
		# 	flag = FlagDocuments.objects.get(flags='None')
		# 	request.POST.get('flags', flag.id)
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
		passport_form = PassportForm(request.POST)
		sbook_form = SBookForm(request.POST)
		coc_form = COCForm(request.POST)
		license_form = LicenseForm(request.POST)
		src_form = SRCForm(request.POST)
		goc_form = GOCForm(request.POST)
		usvisa_form = USVisaForm(request.POST)
		schengenvisa_form = SchengenVisaForm(request.POST)
		yellowfever_form = YellowFeverForm(request.POST)
		# seaservice_form = SeaServiceForm(request.POST)
		# seaservice_form = seaservice_form(request.POST)
		app_form = AppForm(request.POST)
		if appdetails_form.is_valid() and appsource_form.is_valid() and personaldata_form.is_valid() and permanentaddress_form.is_valid() and currentaddress_form.is_valid() and spouse_form.is_valid() and college_form.is_valid() and highschool_form.is_valid() and emergencycontact_form.is_valid() and backgroundinfo_form.is_valid() and passport_form.is_valid() and sbook_form.is_valid() and coc_form.is_valid() and license_form.is_valid() and src_form.is_valid() and goc_form.is_valid() and usvisa_form.is_valid() and schengenvisa_form.is_valid() and yellowfever_form.is_valid() and seaservice_form.is_valid() and app_form.is_valid():
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
			print passport_form.errors
			print sbook_form.errors
			print coc_form.errors
			print license_form.errors
			print src_form.errors
			print goc_form.errors
			print usvisa_form.errors
			print schengenvisa_form.errors
			print yellowfever_form.errors
			print seaservice_form.errors
			print app_form.errors

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
	context_dict['passport_form']= passport_form
	context_dict['sbook_form']= sbook_form
	context_dict['coc_form']= coc_form
	context_dict['license_form']= license_form
	context_dict['src_form']= src_form
	context_dict['goc_form']= goc_form
	context_dict['usvisa_form']= usvisa_form
	context_dict['schengenvisa_form']= schengenvisa_form
	context_dict['yellowfever_form']= yellowfever_form
	context_dict['seaservice_form'] = seaservice_form
	context_dict['app_form']= app_form

	# context_dict["today"] = today

	return render(request, template, context_dict)

@csrf_exempt
def tmp_image(request):
	if request.method == 'POST':
		# does not work with starting slash
		x = 'media/photos/tmp/someimage.jpg'
		f = open(x, 'wb')
		f.write(request.body)
		f.close()
		# os.rename(x, y)
		scheme = request.scheme
		http_host = request.META['HTTP_HOST']
		return HttpResponse(scheme+"://"+http_host+"/"+x)
	else:
		return HttpResponse("No data")