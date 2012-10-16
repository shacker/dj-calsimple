from django.template import RequestContext
from django.shortcuts import render
from django.contrib import messages
from tasks.models import Task
import datetime
from django.utils.timezone import utc

# Use UTC tz support in Django 1.4
now = datetime.datetime.now().replace(tzinfo=utc)
one_day = datetime.timedelta(days=1)
tomorrow = (now + one_day).replace(tzinfo=utc)

def dashboard(request):
	"""
	Display user dashboard
	"""
	tasks_due = Task.objects.filter(user = request.user, due_date_time__lte = now, completed = False)
	tasks_tomorrow = Task.objects.filter(user = request.user, due_date_time__gte = tomorrow.date())
	tasks_upcoming = Task.objects.filter(user = request.user, completed = False, due_date_time__isnull = False).exclude(id__in = [t.id for t in tasks_due]).exclude(id__in = [t.id for t in tasks_tomorrow])
	tasks_unscheduled = Task.objects.filter(user = request.user, due_date_time__isnull = True, completed = False)

	return render(
		request, 'dashboard/dashboard.html', locals()
	)

