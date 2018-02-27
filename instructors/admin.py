# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from instructors.models import Instructors, Position, Course, InstApply
from django.db import models
from django.forms import widgets




class InstructorInline(admin.StackedInline):
    model = Instructors
    fields = ['name', 'surname']
    # описуємо для якої моделі

class PositionAdmin(admin.ModelAdmin):
    inlines = [InstructorInline]


class InstructorAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "position", "is_active"]
    list_display_links = ["name", "surname", "position"]

    list_filter = ['position']
    search_fields = ['name', 'surname']

    list_editable = ["is_active"]

    #fields = ["name", "surname", "email", "position", "date_of_birth", "is_active"]

    #exclude = ["date_of_birth"]
    readonly_fields = ["is_active"]
    raw_id_fields = ["position"]

    save_on_top = True

    fieldsets = [
        (None,                {'fields': ['name', 'surname']}),
        ('Other information', {'fields': ['email', 'date_of_birth', 'position', 'is_active'],
                              'classes': ['collapse']}),
        ]

    formfield_overrides = {
        models.DateField: {'widget': widgets.TextInput}

    }

admin.site.register(Instructors, InstructorAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Course)
admin.site.register(InstApply)
# Register your models here.
