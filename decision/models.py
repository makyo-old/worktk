from django.db import models
from django.contrib.auth.models import User
from worktk.event.models import DateTimeEvent
from worktk.constants import decision_types

class Decision(models.Model):
    timeframe = models.ForeignKey(DateTimeEvent)
    title = models.CharField(max_length = 100)
    body = models.TextField()
    type = models.IntegerField(choices = decision_types)

class DecisionOption(models.Model):
    decision = models.ForeignKey(Decision)
    text = models.TextField()

class BooleanVote(models.Model):
    user = models.ForeignKey(User)
    decision = models.ForeignKey(Decision)
    vote = models.BooleanField()

class OptionVote(models.Model):
    user = models.ForeignKey(User)
    decision = models.ForeignKey(Decision)
    vote = models.ForeignKey(DecisionOption)

class TextVote(models.Model):
    user = models.ForeignKey(User)
    decision = models.ForeignKey(Decision)
    vote = models.CharField(max_length = 500)
