from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404


from jsignature.utils import draw_signature

from . forms import *

import os, shutil

# Create your views here.
def form(request):
	template = "application_form/index.html"
	context_dict = {}
	form = SignatureForm(request.POST or None)
	context_dict['form'] = form
	if request.method == 'POST':
		application_date = request.POST['application-date']
		position_applied = request.POST['position_applied']
		alternative_position = request.POST['alternative_position']
		last_name = request.POST['last_name']
		first_name = request.POST['first_name']
		middle_name = request.POST['middle_name']
		age = request.POST['age']
		birth_date = request.POST['birth_date']
		birth_place = request.POST['birth_place']
		landline_number_1 = request.POST['landline_number_1']
		mobile_number_1 = request.POST['mobile_number_1']
		email_address_1 = request.POST['email_address_1']
		landline_number_2 = request.POST['landline_number_2']
		mobile_number_2 = request.POST['mobile_number_2']
		email_address_2 = request.POST['email_address_2']
		preferred_vessel = request.POST['preferred_vessel']
		availability = request.POST['availability']
		sss = request.POST['sss']
		philhealth = request.POST['philhealth']
		tin = request.POST['tin']
		pag_ibig = request.POST['pag_ibig']
		permanent_street = request.POST['permanent_street']
		permanent_baranggay = request.POST['permanent_baranggay']
		permanent_town = request.POST['permanent_town']
		permanent_municipality = request.POST['permanent_municipality']
		permanent_zip = request.POST['permanent_zip']
		current_street = request.POST['current_street']
		current_baranggay = request.POST['current_baranggay']
		current_town = request.POST['current_town']
		current_municipality = request.POST['current_municipality']
		current_zip = request.POST['current_zip']
		civil_status = request.POST['civil_status']
		date_married = request.POST['date_married']
		spouse_maiden_name = request.POST['spouse_maiden_name']
		spouse_birthday = request.POST['spouse_birthday']
		spouse_contact = request.POST['spouse_contact']
		father_full_name = request.POST['father_full_name']
		mother_full_name = request.POST['mother_full_name']
		tertiary = request.POST['tertiary']
		degree_obtained = request.POST['degree_obtained']
		tertiary_from = request.POST['tertiary_from']
		tertiary_to = request.POST['tertiary_to']
		highschool = request.POST['highschool']
		highschool_from = request.POST['highschool_from']
		highschool_to = request.POST['highschool_to']
		emergency_person = request.POST['emergency_person']
		emergency_contact = request.POST['emergency_contact']
		emergency_relationship = request.POST['emergency_relationship']
		emergency_address = request.POST['emergency_address']
		emergency_zip = request.POST['emergency_zip']
		visa_entry = request.POST['visa_entry']
		leave_order = request.POST['leave_order']
		disciplinary_action = request.POST['disciplinary_action']
		passport_number = request.POST['passport_number']
		passport_expiry = request.POST['passport_expiry']
		sbook_number = request.POST['sbook_number']
		sbook_expiry = request.POST['sbook_expiry']
		coc = request.POST['coc']
		coc_expiry = request.POST['coc_expiry']
		coc_rank = request.POST['coc_rank']
		license = request.POST['license']
		license_rank = request.POST['license_rank']
		src = request.POST['src']
		src_rank = request.POST['src_rank']
		goc_licenses = request.POST['goc_licenses']
		goc_expiry = request.POST['goc_expiry']
		us_visa_expiry = request.POST['us_visa_expiry']
		schengen_visa_expiry = request.POST['schengen_visa_expiry']
		yellow_fever = request.POST['yellow_fever']
		yellow_fever_expiry = request.POST['yellow_fever_expiry']
		essay = request.POST['essay']
		signature = request.POST['signature']

	# context_dict['form'] = form
	return render(request, template, context_dict)