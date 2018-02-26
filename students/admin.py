# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from students.models import Students



class StudentsAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "skype"]

admin.site.register(Students, StudentsAdmin)
