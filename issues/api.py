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
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def issues(request):
	"""
	Create a new issue or get the details for one
	"""
	if request.method == 'GET':
		issues = ''
		try:
			if request.GET['filter_area']:
				lat_sw = request.GET['lat_sw']
				lng_sw = request.GET['lng_sw']
				lat_ne = request.GET['lat_ne']
				lng_ne = request.GET['lng_ne']
				issues = Issue.objects.all().filter(latitude__lte=lat_ne, latitude__gte=lat_sw, longitude__lte=lng_ne, longitude__gte=lng_sw)

			else: issues = Issue.objects.all()
				
		
		except:
			issues = Issue.objects.all()

		logging.debug(issues)
		serializer = IssueSerializer(issues)
		return JSONResponse(serializer.data)

	if request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = IssueSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		else:
			return JSONResponse(serializer.errors, status=400)



