from django.conf.urls import patterns, url

urlpatterns = patterns('issues.views',
    # api calls
    url(r'^issues/new$', 'new'),
    url(r'^issues$', 'create'),
    url(r'^issues/(?P<issue_id>\d+)$', 'get_issue'),
)

urlpatterns += patterns('issues.api',
    url(r'^api/issues$', 'issues'),
)
