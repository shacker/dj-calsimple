from tasks.models import *
from django.contrib import admin
from django.contrib.admin import widgets


class TaskAdmin(admin.ModelAdmin):
    pass

admin.site.register(Task, TaskAdmin)
