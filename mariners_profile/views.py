from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def data_tables(request):
	template = "mariner-profile/index.html"
	context_dict = {}
	return render(request, template, context_dict)

def profile(request):
	template = "mariner-profile/profile.html"
	context_dict = {}
	return render(request, template, context_dict)