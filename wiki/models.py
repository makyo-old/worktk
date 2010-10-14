from django.db import models
from worktk.constants import wiki_page_permissions

class Page(models.Model):
    slug = models.CharField(max_size = 50)
    parent_class = models.CharField(max_size = 50)
    parent_id = models.IntegerField()
    ctime = models.DateTimeField()
    mtime = models.DateTimeField()
    read_permissions = models.IntegerField(choices = wiki_page_permissions)
    edit_permissions = models.IntegerField(choices = wiki_page_permissions)
    version = models.IntegerField()
    title = models.CharField(max_size = 50)
    body = models.TextField()
    # tags = TagField()

class Diff(models.Model):
    page = models.ForeignKey(Page)
    version_from = models.IntegerField()
    diff = models.TextField()
    message = models.CharField(max_size = 500)
    regarding_diff = models.ForeignKey('Diff', null = True)
