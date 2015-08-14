from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from . models import *

def home(request):
	user = request.user
	template = "home.html"
	context_dict = {}
	if user.is_authenticated():
		user = User.objects.get(username=user)
		userprofile = UserProfile.objects.get(user=user)
		userlevel = str(userprofile.userlevel)
		if userlevel == 'recruitment':
			return HttpResponse("HELLO This is the recruitment level!<a href='/logout/'>Log Out</a>")
		elif userlevel == 'applicant':
			return HttpResponse("HELLO This is the applicant level!<a href='/logout/'>Log Out</a>")
		elif userlevel == 'crew':
			return HttpResponse("HELLO This is the crew level!<a href='/logout/'>Log Out</a>")
		else:
			print userlevel
			print type(userlevel)
			return HttpResponse("DEFAULT<a href='/logout/'>Log Out</a>")
	else:
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
