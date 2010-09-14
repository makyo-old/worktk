from django.db import models
from django.contrib.auth.models import User
from worktk.constants import profile_countries, profile_genders

class Employee(models.Model):
    user = models.OneToOneField(User)
    details = models.OneToOneField(Person)
    is_clocked_in = models.BooleanField()

class Profile(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 1, choices = profile_genders, blank = True)
    email = models.EmailField()
    primary_phone = models.CharField(max_length = 20)
    mobile_phone = models.CharField(max_length = 20)
    address1 = models.CharField(max_length = 100)
    address2 = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    postal_code = models.CharField(max_length = 20)
    country = models.IntegerField(choices = countries)
