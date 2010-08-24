from django.db import models
from django.contrib.auth.models import User
from worktk.event.models import DateTimeEvent

class Organization(models.Model):
    members = models.ManyToManyField(User)
    slug = models.SlugField()
    title = models.CharField(max_length = 100)
    description = models.TextField(blank = True)

class Project(models.Model):
    lead = models.ForeignKey(User)
    members = models.ManyToManyField(User)
    slug = models.SlugField()
    title = models.CharField(max_length = 100)

class Component(models.Model):
    project = models.ForeignKey(Project)
    title = models.CharField(max_size = 50)
    description = models.TextField(blank = True)

class Release(models.Model):
    dte = models.ForeignKey(DateTimeEvent)
    title = models.CharField(max_length = 100)
    number = models.CharField(max_length = 20)
