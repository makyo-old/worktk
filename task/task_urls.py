from django.conf.urls.defaults import *

urlpatterns = patterns('worktk.task.views',
    (r'^(?P<task_id>\d+)/$', 'show_task'),
    (r'^create/$', 'create_task'),
    (r'^delete/(?P<task_id>\d+)/$', 'delete_task'),
    (r'^update/(?P<task_id>\d+)/$', 'update_task'),
)
