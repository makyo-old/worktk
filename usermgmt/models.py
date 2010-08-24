from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.ForeignKey(User)
    is_clocked_in = models.BooleanField()
