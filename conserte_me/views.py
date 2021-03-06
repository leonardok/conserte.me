from django.shortcuts import render, render_to_response
from django.template import RequestContext
from issues.models import Issue

def index(request):
    latest_issue_list = Issue.objects.all().order_by('-created_at')[:5]
    total_active = Issue.objects.filter(status=True).count()
    solved_issues = Issue.objects.filter(status=False).count()
    return render_to_response('conserte_me/index.html', {'latest_issue_list': latest_issue_list,
        'total_active': total_active, 'solved_issues': solved_issues}, 
        context_instance=RequestContext(request))


def about_project(request):
    return render_to_response('conserte_me/about_project.html', context_instance=RequestContext(request) )


def about_us(request):
    return render_to_response('conserte_me/about_project.html', context_instance=RequestContext(request) )
