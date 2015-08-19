from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404

from jsignature.utils import draw_signature

# from application_form.forms import SignatureForm, SampleForm
# from application_form.models import JSignatureModel

from . models import *

# import os, shutil

# def signature(request):
# 	template = "application_form/index.html"
# 	context_dict = {}
# 	form = SignatureForm(request.POST or None)
# 	# sample_form = SampleForm(request.POST or None)
# 	context_dict['form'] = form
# 	# context_dict['sample_form'] = sample_form
# 	if form.is_valid():
# 		signature = form.cleaned_data.get('signature')
# 		# print signature
# 		if signature:
# 			# as an image
# 			signature_picture = draw_signature(signature)
# 			#or as a file
# 			_signature_file_path = draw_signature(signature, as_file=True)
# 			signature_file_path = settings.MEDIA_ROOT+"/signatures/"
# 			shutil.move(_signature_file_path, signature_file_path)
# 			_signature_file_path = _signature_file_path.replace('/tmp/', 'signatures/')

# 			signature = JSignatureModel.objects.get_or_create(name='sample')[0]
# 			signature.signatures = _signature_file_path
# 			signature.save()
# 	else:
# 		print form.errors
# 	# if sample_form.is_valid():
# 	# 	print "armada"
# 	# 	sample_form = sample_form.save(commit=False)
# 	# 	if 'picture' in request.FILES:
# 	# 		print "guinto"
# 	# 		print request.FILES['picture']
# 	# 		picture = request.FILES['picture']
# 	# 	else:
# 	# 		picture = ''
# 	# 	sample_form.picture = picture
# 	# 	sample_form.save()
		
# 	# else:
# 	# 	print "dean"
# 	# 	# print sample_form
# 	# 	print sample_form.errors
# 	return render(request, template, context_dict)

def home(request):
	user = request.user
	template = "home.html"
	context_dict = {}
	context_dict = {"title": "Manship People Software"}
	if user.is_authenticated():
		user = User.objects.get(username=user)
		userprofile = UserProfile.objects.get(user=user)
		userlevel = str(userprofile.userlevel)
		if userlevel == 'recruitment':
			# return signature(request)
			return HttpResponse("HELLO This is the recruitment level!<a href='/logout/'>Log Out</a>")
		elif userlevel == 'applicant':
			# return HttpResponse("HELLO This is the applicant level!<a href='/logout/'>Log Out</a>")
			return HttpResponseRedirect('/application-form/')
		elif userlevel == 'crew':
			return HttpResponse("HELLO This is the crew level!<a href='/logout/'>Log Out</a>")
		else:
			print userlevel
			print type(userlevel)
			return HttpResponse("DEFAULT<a href='/logout/'>Log Out</a>")
	return render(request, template, context_dict)

def validation(request):
	username = ''
	password = ''
	if request.method == 'POST':
		if 'username' in request.POST and 'password' in request.POST:
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(username=username, password=password)
			if user:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponseRedirect('/?error=Invalid Username or Password')
		else:
			return HttpResponseRedirect('/?error=Invalid LogIn Attempt')
	else:
		# raise Http404
		return HttpResponseRedirect('/?error=Invalid LogIn Attempt')

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')
