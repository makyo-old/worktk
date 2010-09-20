from django.db import models
from django.contrib.auth.models import Group
from worktk.usermgmt.models import Employee
from worktk.event.models import DateTimeEvent

class OrganizationMember(models.Model):
    organization = models.ForeignKey('Organization')
    member = models.ForeignKey(Employee)
    role = models.ManyToManyField('OrganizationRole')

class OrganizationRole(models.Model):
    organization = models.ForeignKey('Organization')
    title = models.CharField(max_length = 50)
    description = models.TextField(blank = True)

class Organization(models.Model):
    members = models.ManyToManyField(OrganizationMember)
    board = models.ForeignKey(OrganizationRole)
    slug = models.SlugField()
    title = models.CharField(max_length = 100)
    description = models.TextField(blank = True)

class Project(models.Model):
    lead = models.ForeignKey(Employee)
    members = models.ManyToManyField(Employee)
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
