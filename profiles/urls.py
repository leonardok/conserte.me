from django.conf.urls import patterns, url

urlpatterns = patterns('profiles.views',
    url(r'^new/$', 'new'),
    url(r'^create/$', 'create'),
    url(r'^show/$', 'show', name="show_profile"),
)

urlpatterns += patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
)
