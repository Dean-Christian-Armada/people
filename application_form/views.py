from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.forms.formsets import formset_factory
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from easy_pdf.views import PDFTemplateView
from easy_pdf.rendering import render_to_pdf_response

from jsignature.utils import draw_signature

from . forms import *

import os, shutil, datetime

# Create your views here.
# Take notes Logic of form save is in the forms.py save method of own FormObjects


@login_required()
def form(request):
	applicant_name = ApplicantNameForm()
	personal_data = PersonalDataForm()
	permanent_address = PermanentAddresForm()
	current_address = CurrentAddresForm()

	if request.method == "POST":
		print request.POST
		applicant_name = ApplicantNameForm(request.POST)
		permanent_address = PermanentAddresForm(request.POST)
		current_address = CurrentAddresForm(request.POST)
		personal_data = PersonalDataForm(request.POST)

		if applicant_name.is_valid() and personal_data.is_valid():
			applicant_name_object
			personal_data.save()
		else:
			print applicant_name.errors
			print personal_data.errors

	template = "application_form/index.html"
	context_dict = {"title": "Application Form"}
	context_dict['applicant_name'] = applicant_name
	context_dict['permanent_address'] = permanent_address
	context_dict['current_address'] = current_address
	context_dict['personal_data'] = personal_data

	return render(request, template, context_dict)