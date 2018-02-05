# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from courses.models import Courses, Lesson


def courses_list(request):
    courses = Courses.objects.all()
    lessons = Lesson.objects.all()
    return render(request, "courses.html", {"courses_list": courses,
                                            'lessons_list': lessons})
