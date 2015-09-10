from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.forms.formsets import formset_factory, BaseFormSet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from easy_pdf.views import PDFTemplateView
from easy_pdf.rendering import render_to_pdf_response

from jsignature.utils import draw_signature

from . forms import *

from mariners_profile.models import TrainingCertificatesSegregation

import os, shutil, datetime, random, string



# Create your views here.
# Take notes Logic of form save is in the forms.py save method of own FormObjects


# Enables field required on formset even without filling up a singlefield
# class RequiredFormSet(BaseFormSet):
#     def __init__(self, *args, **kwargs):
#         super(RequiredFormSet, self).__init__(*args, **kwargs)
#         for form in self.forms:
#             form.empty_permitted = False

# Enables field required on the first form
class FirstRequiredFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(FirstRequiredFormSet, self).__init__(*args, **kwargs)
        self.forms[0].empty_permitted = False
        # for form in self.forms:
        #     form.empty_permitted = False

@login_required()
def form(request):
	scheme = request.scheme
	http_host = request.META['HTTP_HOST']
	application = ApplicationForm()

	# emergency_contact = EmergencyContactForm()

	if request.method == "POST":
		application = ApplicationForm(request.POST)

		if application.is_valid():
			application.save()
			# Webcam script on saving in a folder
			first_name = request.POST['first_name']
			middle_name = request.POST['middle_name']
			last_name = request.POST['last_name']
			file_name = first_name+middle_name+last_name
			file_name = "".join(file_name.split())
			try:
				tmp_application_picture = request.POST['application_picture']
				tmp_application_picture = tmp_application_picture.replace(scheme+"://"+http_host+"/", "")
				print tmp_application_picture
				application_picture = "media/photos/"+file_name+".jpg"
				os.rename(tmp_application_picture, application_picture)
				application_picture = application_picture.replace("media/", "")
			except:
				pass
			signature_path = "media/signature/"+file_name+".png"
			if signature:
				signature_picture = draw_signature(signature)
				_signature_file_path = draw_signature(signature, as_file=True)
				signature_file_path = settings.MEDIA_ROOT+"/signatures/"
				shutil.move(_signature_file_path, signature_file_path)
				_signature_file_path = _signature_file_path.replace('/tmp/', 'signatures/')
			
		else:
			print application.errors
			

	template = "application_form/index.html"
	context_dict = {"title": "Application Form"}
	context_dict['application'] = application



	return render(request, template, context_dict)


@login_required
def success(request):
	template = "application_form/success.html"
	context_dict = {"title": "Thank You For Applying at Manship"}
	return render(request, template, context_dict)

@csrf_exempt
@login_required
def tmp_image(request):
	if request.method == 'POST':
		tmp_image_name = ''.join(random.choice(string.lowercase) for i in range(10))
		# does not work with starting slash
		x = 'media/photos/tmp/'+tmp_image_name+'.jpg'
		# y = 'media/photos/image.jpg'
		f = open(x, 'wb')
		f.write(request.body)
		f.close()
		# os.rename(x, y)
		scheme = request.scheme
		http_host = request.META['HTTP_HOST']
		return HttpResponse(scheme+"://"+http_host+"/"+x)
	else:
		return HttpResponse("No data")