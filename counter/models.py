from django.db import models
from django.contrib.auth.models import User
from worktk.event.models import DateTimeEvent
from worktk.project.models import Project

class Counter(models.Model):
    dte = models.ForeignKey(DateTimeEvent)
    title = models.CharField(max_length = 50)
    owner = models.ForeignKey(User)
    project = models.ForeignKey(Project, null = True)
    count = models.IntegerField()
