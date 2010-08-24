from django.db import models
from django.contrib.auth.models import User
from worktk.event.models import DateTimeEvent
from worktk.project.models import Project, Component, Release

class Task(models.Model):
    dte = models.ForeignKey(DateTimeEvent, null = True)
    submitter = models.ForeignKey(User, null = True)
    owner = models.ForeignKey(User)
    component = models.ForeignKey(Component, null = True)
    release = models.ForeignKey(Release, null = True)
    parent = models.ForeignKey('Task', null = True)
    title = models.CharField(max_length = 100, blank = False)
    description = models.TextField(blank = True)
