from django.db import models

class Tasks(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True,null=True)

    class Meta:
        verbose_name_plural = "Tasks and Assignments"

    def __unicode__(self):
      return self.name