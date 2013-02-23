from django.template import Context, loader
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from issues.models import Issue, City, State, Country
from issues.serializers import IssueSerializer
from django.shortcuts import render
from django.db.models import Q
import logging
import re

# Create your views here.

def index(request):
	issues = Issue.objects.all()
	logging.debug(issues)
	return render(request, 'issues/index.html', {'issues': issues})



def show(request, issue_id):
	issue = Issue.objects.get(id=issue_id)
	comments = ''
	return render(request, 'issues/show.html', {'issue': issue})
	

def search(request, country, state, city):
	city_normal = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', city)
	try:
		issues = Issue.objects.filter( city= City.objects.get( name=city_normal, state= State.objects.get( name=state, country= Country.objects.get(name=country) ) ) )
	except:
		issues = Issue.objects.none()
	logging.debug (city_normal)
	return render(request, 'issues/index.html', {'city': city_normal, 'state': state, 'issues': issues})

def new(request):
	return render(request, 'issues/new.html')


def create(request):
	if request.method == 'POST':
		try:
			name = request.POST['name']
			description = request.POST['description']
			lat = request.POST['latitude']
			lng = request.POST['longitude']

		except:
			raise Http404

		issue = Issue()
		issue.name = name
		issue.description = description

		logging.debug('Debug latitude')

		issue.latitude = lat
		issue.longitude= lng
		
		issue.save()
		try:
			logging.debug('Saving issue')
			issue.save()
		except:
			raise Http404
		
		return render(request, 'issues/show.html', {'issue': issue})



