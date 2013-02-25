from django.template import Context, loader
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from issues.models import Issue, City, State, Country
from issues.serializers import IssueSerializer
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
	page = request.GET.get('page')
	logging.debug ('Page: ' + str(page))
	city_normal = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', city)

	issues = Issue.objects.none()

	try:
		issue_objects = Issue.objects.filter( city= City.objects.get( name=city_normal, state= State.objects.get( name=state, country= Country.objects.get(name=country) ) ) )
		logging.debug (issue_objects)

		paginator = Paginator(issue_objects, 20)
		logging.debug (paginator)

		page = paginator.page(int(page))

		issues = page
		logging.debug (paginator.page(page))
	except PageNotAnInteger:
		logging.debug ('Page not an integer')
	except EmptyPage:
		logging.debug ('Page empty')

	logging.debug (city_normal)
	return render(request, 'issues/index.html', {'city': city_normal, 'state': state, 'issues': issues, 'page': page})


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



