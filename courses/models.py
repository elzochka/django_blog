# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Courses(models.Model):
    name = models.CharField(verbose_name=u'Course Name', max_length=255, help_text="This is course name")
    short_description = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(verbose_name=u'Lesson Name', max_length=255, help_text="This is lesson name")
    description = models.TextField()
    course = models.ForeignKey(Courses)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.subject

