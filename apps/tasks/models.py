from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.timezone import utc


SOURCE_CHOICES = (
	('canvas-assignments','Canvas Assignments'),
	('google-tasks','Google Tasks'),
)

class Task(models.Model):
	"""
	A task or assignment for a user, sourced from Canvas or Google Tasks
	"""

	user = models.ForeignKey(User)
	due_date_time = models.DateTimeField(blank=True, null=True)
	source = models.CharField(choices=SOURCE_CHOICES, max_length=30)
	title = models.CharField(max_length=140, null=False)
	url = models.URLField(null=True, blank=True)
	course_title = models.CharField(max_length=140, blank=True, null=True) # Later this will be FK to a Course object
	course_url = models.URLField(null=True, blank=True)
	in_progress = models.BooleanField(default=False)
	completed = models.BooleanField(default=False)

	def overdue(self):
		"Returns true if task is overdue"
		if self.due_date_time < datetime.datetime.now().replace(tzinfo=utc) :
			return True

	class Meta:
		verbose_name = 'Tasks'
		verbose_name_plural = 'Tasks'

	class Admin:
		pass

	def __unicode__(self):
		return self.title
