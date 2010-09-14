from django.db import models
from django.contrib.auth.models import User
from worktk.event.models import DateTimeEvent
from worktk.project.models import Project, Component, Release
from worktk.support.models import KBEntry
from worktk.constants import task_types, task_priorities, task_statuses, task_agile_lanes, task_resolutions, taskaction_actions

class Task(models.Model):
    submitter = models.ForeignKey(User, null = True)
    assignee = models.ForeignKey(User)
    component = models.ForeignKey(Component, null = True)
    fix_by_release = models.ForeignKey(Release, null = True)
    affects_releases = models.ManyToManyField(Release, null = True)
    parent = models.ForeignKey('Task', null = True)
    duplicate_of = models.ForeignKey('Task', null = True, related_name = 'duplicates')
    title = models.CharField(max_length = 100, blank = False)
    description = models.TextField(blank = True)
    task_type = models.IntegerField(choices = task_types)
    priority = models.IntegerField(choices = task_priorities)
    status = models.IntegerField(choices = task_statuses)
    agile_lane = models.IntegerField(choices = task_agile_lanes)
    resolution = models.IntegerField(choices = task_resolutions)
    agile_dte = models.ForeignKey(DateTimeEvent, null = True)
    ctime = models.DateTimeField(auto_now_add = True)
    rtime = models.DateTimeField(null = True) #resolved
    kb = models.ForeignKey(KBEntry)

class TaskAction(models.Model):
    task = models.ForeignKey(Task)
    user = models.ForeignKey(User)
    ctime = models.DateTimeField(auto_now_add = True)
    action = models.IntegerField(choices = taskaction_actions)
    value_from = models.TextField(blank = True)
    value_to = models.TextField(blank = True)
