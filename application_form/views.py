from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.forms.formsets import formset_factory, BaseFormSet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from easy_pdf.views import PDFTemplateView
from easy_pdf.rendering import render_to_pdf_response

from jsignature.utils import draw_signature

from . forms import *

import os, shutil, datetime

# Create your views here.
# Take notes Logic of form save is in the forms.py save method of own FormObjects

# Enables field required on formset even without filling up a singlefield
class RequiredFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False

@login_required()
def form(request):
	applicant_name = ApplicantNameForm()
	personal_data = PersonalDataForm()
	permanent_address = PermanentAddressForm()
	current_address = CurrentAddressForm()
	spouse = SpouseForm()
	college = formset_factory(CollegeForm, extra=1, formset=RequiredFormSet)
	highschool = HighSchoolForm()
	emergency_contact = formset_factory(EmergencyContactForm, extra=1, formset=RequiredFormSet)
	visa_application = VisaApplicationForm()
	detained = DetainedForm()
	disciplinary_action = DisciplinaryActionForm()
	passport = PassportForm()
	sbook = SbookForm()
	coc = COCForm()
	license = LicenseForm()
	src = SRCForm()
	goc = GOCForm()
	us_visa = USVisaForm()
	schengen_visa = SchengenVisaForm()
	yellow_fever = YellowFeverForm()
	flags = FlagForm()
	# emergency_contact = EmergencyContactForm()

	if request.method == "POST":
		print request.POST
		applicant_name = ApplicantNameForm(request.POST)
		permanent_address = PermanentAddressForm(request.POST)
		current_address = CurrentAddressForm(request.POST)
		personal_data = PersonalDataForm(request.POST)
		spouse = SpouseForm(request.POST)
		college = college(request.POST)
		highschool = HighSchoolForm(request.POST)
		emergency_contact = emergency_contact(request.POST)
		visa_application = VisaApplicationForm(request.POST)
		detained = DetainedForm(request.POST)
		disciplinary_action = DisciplinaryActionForm(request.POST)
		passport = PassportForm(request.POST)
		sbook = SbookForm(request.POST)
		coc = COCForm(request.POST)
		license = LicenseForm(request.POST)
		src = SRCForm(request.POST)
		goc = GOCForm(request.POST)
		us_visa = USVisaForm(request.POST)
		schengen_visa = SchengenVisaForm(request.POST)
		yellow_fever = YellowFeverForm(request.POST)
		flags = FlagForm(request.POST)
		# emergency_contact = EmergencyContactForm(request.POST)


		if applicant_name.is_valid() and personal_data.is_valid() and permanent_address.is_valid() and current_address.is_valid() and spouse.is_valid() and college.is_valid() and highschool.is_valid() and emergency_contact.is_valid() and visa_application.is_valid() and detained.is_valid() and disciplinary_action.is_valid() and passport.is_valid() and sbook.is_valid()and coc.is_valid()and license.is_valid()and src.is_valid()and goc.is_valid()and us_visa.is_valid()and schengen_visa.is_valid()and yellow_fever.is_valid() and flags.is_valid():
			applicant_name.save()
			permanent_address.save()
			current_address.save()
			personal_data.save()
			spouse.save()
			for college_form in college:
				college_form.save()
			highschool.save()
			for emergency_contact_form in emergency_contact:
				emergency_contact_form.save()
			# emergency_contact.save()
			visa_application.save()
			detained.save()
			disciplinary_action.save()
			passport.save()
			sbook.save()
			coc.save()
			license.save()
			src.save()
			goc.save()
			us_visa.save()
			schengen_visa.save()
			yellow_fever.save()
			flags.save()
			flags.save_m2m()
		else:
			print applicant_name.errors
			print permanent_address.errors
			print current_address.errors
			print personal_data.errors
			print spouse.errors
			print college.errors
			print highschool.errors
			print emergency_contact.errors
			print visa_application.errors
			print detained.errors
			print disciplinary_action.errors
			print passport.errors
			print sbook.errors
			print coc.errors
			print license.errors
			print src.errors
			print goc.errors
			print us_visa.errors
			print schengen_visa.errors
			print yellow_fever.errors
			print flags.errors

	template = "application_form/index.html"
	context_dict = {"title": "Application Form"}
	context_dict['applicant_name'] = applicant_name
	context_dict['permanent_address'] = permanent_address
	context_dict['current_address'] = current_address
	context_dict['personal_data'] = personal_data
	context_dict['spouse_form'] = spouse
	context_dict['college'] = college
	context_dict['highschool_form'] = highschool
	context_dict['emergency'] = emergency_contact
	context_dict['visa_application'] = visa_application
	context_dict['detained'] = detained
	context_dict['disciplinary_action'] = disciplinary_action
	context_dict['passport_form'] = passport
	context_dict['sbook_form'] = sbook 
	context_dict['coc_form'] = coc 
	context_dict['license_form'] = license 
	context_dict['src_form'] = src 
	context_dict['goc_form'] = goc 
	context_dict['usvisa_form'] = us_visa 
	context_dict['schengenvisa_form'] = schengen_visa 
	context_dict['yellowfever_form'] = yellow_fever
	context_dict['flags'] = flags
	return render(request, template, context_dict)