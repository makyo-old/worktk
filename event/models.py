from django.db import models
from django.contrib.auth.models import User

class DateTimeEvent(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null = True)

class TimeClockEvent(models.Model):
    dte = models.ForeignKey(DateTimeEvent)
    owner = models.ForeignKey(User)

class Event(models.Model):
    dte = models.ForeignKey(DateTimeEvent)
    owner = models.ForeignKey(User)
    calendar = modelsForegnKey(Calendar)
    title = models.CharField(max_length = 50, blank = False)
    description = models.TextField(blank = True)

class Calendar(models.Model):
    owner = models.ForeignKey(User)
    slug = models.SlugField()
    title = models.CharField(max_length = 50, blank = False)
    description = models.TextField(blank = True)
