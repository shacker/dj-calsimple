from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib import admin

# Enable the Admin:
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'index.html'}, name='index',),
    url(r'^feeder/$', 'feeder.views.flickr_feed', name='flickr_feed',),

    url(r'^dashboard/', include('dashboard.urls')),
    (r'^people/', include('people.urls')),

    # Admin and Admin docs
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Google API pass-through
    # (r'^tasks$', 'gapi.views.cc_gapi'),
    # (r'^oauth2callback', 'gapi.views.auth_return'),

)
