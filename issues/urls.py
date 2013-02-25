from django.conf.urls import patterns, url

urlpatterns = patterns('issues.views',
    # api calls
    url(r'^issues/new/$', 'new'),
    url(r'^issues/create/$', 'create'),
    url(r'^issues/(?P<issue_id>\d+)/$', 'show', name="issue_show"),
    url(r'^issues/$', 'index'),
    url(r'^issues/([A-Z]{2})/([A-Z]{2})/([A-Za-z]+)/$', 'search'),
)

urlpatterns += patterns('issues.api',
    url(r'^api/issues/$', 'issues'),
    url(r'^api/issues/(?P<issue_id>\d+)/$', 'get'),
)
