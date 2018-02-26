# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from courses.models import Courses, Lesson

class LessonAdminInline(admin.TabularInline):
    model = Lesson
    list_display = ["subject"]



class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonAdminInline]
    list_display = ["name",  "short_description"]
    search_fields = ['name']
    list_display_links = ['name']




admin.site.register(Courses, CourseAdmin)