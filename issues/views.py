from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from issues.models import Issue
from issues.serializers import IssueSerializer
from django.shortcuts import render

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
def issue(request):
	"""
	Create a new issue or get the details for one
	"""
	if request.method == 'GET':
		issues = Issue.objects.all()
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



def new(request):
	return render(request, 'mobile.html')
