from django.conf.urls import patterns, url

urlpatterns = patterns('issues.views',
    # url(r'^api/issues/(?P<pk>[0-9]+)/$', 'snippet_detail'),
    url(r'^api/issues$', 'issue'),
    url(r'^issues/new$', 'new'),
)

