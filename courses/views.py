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

def main_page(request):
    courses = Courses.objects.all()
    return render(request, "main_page.html", {"courses_list": courses})

def courses_main_page(request):
    return render(request, "courses_main_page.html")