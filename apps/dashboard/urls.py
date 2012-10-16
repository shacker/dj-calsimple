from django.conf.urls import patterns, include, url
from dashboard.models import *

# Dashboard URLs
urlpatterns = patterns('dashboard.views',
    url(r'^$', 'dashboard', name="dashboard"),
)

