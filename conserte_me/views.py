from django.shortcuts import render, render_to_response
from issues.models import Issue

def index(request):
	latest_issue_list = Issue.objects.all().order_by('-created_at')[:5]
	total_active = Issue.objects.filter(open__exact=True).count()
	solved_issues = Issue.objects.filter(open__exact=False).count()
	return render_to_response('index.html', {'latest_issue_list': latest_issue_list,
		'total_active': total_active,
		'solved_issues': solved_issues})
