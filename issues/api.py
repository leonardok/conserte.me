from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from issues.models import Issue, Follower, Photo
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
def add_follower(request):
	try:
		data = json.loads(request.raw_post_data)
		logging.debug('Creating follower for issue id:' + str(data['id']) + '; ' + str(data['email']) )

		follower = Follower.objects.create(email=data['email'], issue_id=data['id'])
		follower.save()
	except Exception, e:
		return JSONResponse("Error adding folower to issue: " + str(e), status=400)

	return JSONResponse("Added follower", status=200)




@csrf_exempt
def issues(request):
	"""
	Create a new issue or get the details for one
	"""
	logging.debug('####################### Started API issues #######################')
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
		logging.debug("POST DUMP ---- " + request.raw_post_data )
		logging.debug("JSON DUMP ---- " + str(json.loads(request.raw_post_data ) ) )

		try:
			data = json.loads( str(request.raw_post_data) )
		except:
			return JSONResponse("Could not parse JSON", status=400)

		logging.debug("PARSED JSON DUMP ---- " + str(data) )
			
		serializer = IssueSerializer(data=data["issue"])
		if serializer.is_valid():
			serializer.save()

			logging.debug("RESPONSE ---- " + str(serializer.data) )
			return JSONResponse(serializer.data, status=200)
		else:
			return JSONResponse(serializer.errors, status=400)



def get(request, issue_id):
	if request.method == 'GET':
		issue = Issue.objects.get(id=issue_id)
		serializer = IssueSerializer(issue)
		return JSONResponse(serializer.data)

	raise Http404
