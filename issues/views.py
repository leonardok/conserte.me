from django.template import Context, RequestContext, loader
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from issues.models import Issue, City, State, Country, Photo
from issues.serializers import IssueSerializer
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from easy_thumbnails.files import get_thumbnailer, generate_all_aliases

from django.contrib.auth.decorators import login_required

import logging
import re

# Create your views here.

def index(request):
    issues = Issue.objects.all().filter(is_public=True)
    logging.debug(issues)

    return  render_to_response('issues/index.html', { 'issues': issues }, context_instance=RequestContext(request))



def show(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    issue.page_hits += 1
    issue.save()

    issue.photos = issue.photo_set.all().filter(is_public=True)
    logging.debug(issue)

    c = RequestContext(request, { 'issue': issue })
    return render(request, 'issues/show.html', c)
    

def search(request, country, state, city):
    page = request.GET.get('page')
    logging.debug ('Page: ' + str(page))
    city_normal = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', city)

    issues = Issue.objects.none()

    try:
        issue_objects = Issue.objects.filter( city= City.objects.get( name=city_normal, state= State.objects.get( name=state, country= Country.objects.get(name=country) ) ), is_public=True )
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
    c = RequestContext(request, { 'city': city_normal, 'state': state, 'issues': issues, 'page': page })
    return render(request, 'issues/index.html', c )


@login_required
def new(request):
    return render(request, 'issues/new.html')


@login_required
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

            # send email
            issue.new_issue_email()
        except:
            raise Http404

        return render(request, 'issues/show.html', {'issue': issue})



@csrf_exempt
def add_photo(request):
    logging.debug('ADD PHOTO')

    if request.method == 'POST':
        logging.debug(request.POST)
        logging.debug(request.FILES['photo_file'])
        photo = Photo.objects.create(photo = request.FILES['photo_file'], issue_id=request.POST['issue_id'])
        photo.save()

        return redirect('/issues/' + request.POST['issue_id'])
    else:
        return render(request, 'issues/show.html', {'issue': Issue.objects.get(id=request.POST['issue_id']), 'error': 'Some error occured'})



