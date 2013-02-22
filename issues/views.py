from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from issues.models import Issue
from issues.serializers import IssueSerializer
from django.shortcuts import render
from django.db.models import Q
import logging

# Create your views here.

def get_issue(request, issue_id):
	issue = Issue.objects.get(id=issue_id)
	comments = ''
	return render(request, 'issue_details.html', {'issue': issue})
	


def new(request):
	return render(request, 'mobile.html')


def create(request):
	if request.method == 'POST':
		try:
			name = request.POST['name']
			description = request.POST['description']
			lat = request.POST['latitude']
			lng = request.POST['longitude']

		except:
			from django.http import Http404

		issue = Issue.objects.create()
		issue.name = name
		issue.description = description
		issue.latitude = lat
		issue.longitude= lng
		
		try:
			issue.save()
		except:
			from django.http import Http404
		
		return render(request, 'issue_details.html', {'issue': issue})



