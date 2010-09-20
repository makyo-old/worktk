from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Counter app
    (r'^(ctr|counter)/', include('worktk.counter.counter_urls')),

    # Decision app
    (r'^(d|dcn|decision)/', include('worktk.decision.decision_urls')),

    # Event app
    (r'^(c|cal|calendar)/', include('worktk.event.calendar_urls')),
    (r'^(tce|timeclock)/', include('worktk.event.timeclock_urls')),
    (r'^(e|evt|event)/', include('worktk.event.event_urls')),

    # Project app
    (r'^(o|org|organization)/', include('worktk.project.organization_urls')),
    (r'^(p|prj|project)/', include('worktk.project.project_urls')), #includes component & release

    # Task app
    (r'^(t|task)/', include('worktk.task.task_urls')),

    # Support app
    (r'^(s|sup|support)/', include('worktk.support.support_urls')),
    (r'^kb/'), include('worktk.support.kb_urls')),

    # User app
    (r'^(u|user)/', include('worktk.usermgmt.user_urls')),
    (r'^accounts/', include('worktk.usermgmt.account_urls')),

    (r'^admin/', include(admin.site.urls)),
)
