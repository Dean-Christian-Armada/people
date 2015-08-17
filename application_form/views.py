from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404


from jsignature.utils import draw_signature

from . forms import *

import os, shutil

# Create your views here.
def form(request):
	template = "application_form/index.html"
	context_dict = {}
	form = AppDetailsForm(request.POST or None)

	context_dict['form'] = form
	return render(request, template, context_dict)