from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Template, Context
from checkyourgender.forms import InputForm
import requests
import json
def home(request):
	d = {'title': 'GenderFinder :: The Form'}
	form = InputForm(request.POST or None)
	if form.is_valid():
		data = form.cleaned_data
		name = requests.get("http://api.genderize.io/?name=" + data['name'])
		gender = json.loads(name.text)
		gender = gender['gender']
		d['name'] = data['name']
		d['gender'] = gender
	else:
		d['form'] = form
	return render(request, 'home.html', d)