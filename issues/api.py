from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from issues.models import Issue
from issues.serializers import IssueSerializer
from django.shortcuts import render
from django.db.models import Q
import logging

# For json
import simplejson as json

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
		logging.debug(request.raw_post_data)
		logging.debug(json.loads(request.raw_post_data))
		try:
			data = json.loads(request.raw_post_data)
		except:
			return JSONResponse("Could not parse JSON", status=400)
			
		serializer = IssueSerializer(data=data['issue'])
		if serializer.is_valid():
			serializer.save()

			response = {'issue': serializer.data}
			return JSONResponse(response, status=201)
		else:
			return JSONResponse(serializer.errors, status=400)



def get(request, issue_id):
	if request.method == 'GET':
		issue = Issue.objects.get(id=issue_id)
		serializer = IssueSerializer(issue)
		return JSONResponse(serializer.data)

	raise Http404