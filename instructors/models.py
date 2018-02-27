# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class InstApply(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    package = models.CharField(max_length=10)
    new_subscribe = models.BooleanField()
    comment = models.TextField()
    is_active = models.BooleanField(default=True)
    date_apply = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Instructors(models.Model):
    name = models.CharField(verbose_name=u'Instructor Name', max_length=255, help_text="This is name")
    surname = models.CharField(max_length = 255)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True)

    course = models.ManyToManyField(Course)
    is_active = models.BooleanField(default=True)

    position = models.ForeignKey(Position, null=True)

    def __str__(self):
        return self.name