# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Instructors(models.Model): # має бути Instructorале в дб пишеться уже з буквою с
    name = models.CharField(max_length = 64)
    surname = models.CharField(max_length = 64)
    cource = models.CharField(max_length = 64)