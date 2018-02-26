# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from students.models import Students

def main_page(request):
    students = Students.objects.all()
    return render(request, "main_page.html")
