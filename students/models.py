# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from courses.models import Courses
# Create your models here.

class Students(models.Model):
    first_name = models.CharField(verbose_name=u'Student Name', max_length=255, help_text="This is name")
    last_name = models.CharField(verbose_name=u'Student Surname', max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=50, help_text="Write your phone number here")
    address = models.CharField(max_length=255, null=True, blank=True)
    skype = models.CharField(max_length=50,unique=True, null=True)
    courses = models.ManyToManyField(Courses)
