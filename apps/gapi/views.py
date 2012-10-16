import os
import logging
import httplib2

from apiclient.discovery import build
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django_sample.plus.models import CredentialsModel
from django_sample import settings
from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.django_orm import Storage

# CLIENT_SECRETS, name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret, which are found
# on the API Access tab on the Google APIs
# Console <http://code.google.com/apis/console>
CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), '..', 'client_secrets.json')

# This is dirty and needs refactoring - because the scope is different in the flow,
# and flow is used in multiple functions.

FLOW_TASKS = flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/tasks',
    redirect_uri='http://localhost:8000/oauth2callback'
    )

FLOW_CALENDAR = flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/cal',
    redirect_uri='http://localhost:8000/oauth2callback'
    )


@login_required
def cc_gapi(request):
  storage = Storage(CredentialsModel, 'id', request.user, 'credential')
  credential = storage.get()

  if credential is None or credential.invalid == True:
    FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY, request.user)
    authorize_url = FLOW.step1_get_authorize_url()
    return HttpResponseRedirect(authorize_url)
  else:
    http = httplib2.Http()
    http = credential.authorize(http)

    # Build the correct API service for tasks or calendar
    service = build(gapi_type, 'v1', http=http)
    if gapi_type == 'tasks':
      itemlist = service.tasks().list(tasklist='@default').execute()
    else:
      pass

    return render_to_response('plus/welcome.html', {
      'itemlist': itemlist,
    })


@login_required
def auth_return(request):
  if not xsrfutil.validate_token(settings.SECRET_KEY, request.REQUEST['state'], request.user):
    return HttpResponseBadRequest()

  credential = FLOW.step2_exchange(request.REQUEST)
  storage = Storage(CredentialsModel, 'id', request.user, 'credential')
  storage.put(credential)
  return HttpResponseRedirect("/")
