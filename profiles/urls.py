from django.conf.urls import patterns, url

urlpatterns = patterns('profiles.views',
    url(r'^create/$', 'create', name="profile_create"),
    url(r'^show/$', 'show', name="profile_show"),
)

urlpatterns += patterns('',
)
