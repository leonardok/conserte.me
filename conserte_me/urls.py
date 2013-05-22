from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'conserte_me.views.home', name='home'),
    # url(r'^conserte_me/', include('conserte_me.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'conserte_me.views.index', name='home'),
    url(r'^about/project/$', 'conserte_me.views.about_project', name='about_project'),
    url(r'^about/us/', 'conserte_me.views.about_us', name='about_us'),
    url(r'^', include('issues.urls', app_name="issues")),

    url(r'^comments/', include('django.contrib.comments.urls')),

    url(r'^assets/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT, }),
)
