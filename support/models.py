from django.db import models
from django.contrib.auth.models import User
from worktk.usermgmt.models import Profile, Employee
from worktk.project.models import Project, Component
from worktk.event,models import DateTimeEvent
from worktk.task.models import Task
from worktk.constants import ticket_statuses

class CustomerContact(models.Model):
    profile = models.ForeignKey(Profile)
    project = models.ForeignKey(Project)
    implementation = models.TextField()    

class Ticket(models.Model):
    entered_by = models.ForeignKey(User)
    assignee = models.ForeignKey(Employee, blank = True, null = True)
    component = models.ForeignKey(Component)
    ctime = models.DateTimeField(auto_now_add = True)
    mtime = models.DateTimeField(auto_now = True)
    rtime = models.DateTimeField(null = True)
    status = models.IntegerField(choices = ticket_statuses)
    description = models.TextField()
    resolution = models.TextField()
    task = models.ForeignKey(Task)
    #tags = TagField()
    kb = models.ForeignKey(KBEntry)

class KBEntry(models.Model):
    component = models.ForeignKey(Component)
    first_affected_release = models.ForeignKey(Release)
    fixed_release = models.ForeignKey(Release, related_name = 'fixes_kbs')
    title = models.CharField(max_length = 100)
    text = models.TextField()
    #tags = TagField()
