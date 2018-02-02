# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from instructors.models import Instructors


def hello(request):
    return render(request, "index.html")

def http(request):
    return render(request, "http.html")


def hello_python(request, some):
    return HttpResponse("Hello python!!" + some)

def sum_two(request, a, b):
    s = int(a) + int(b)
    return HttpResponse(s)

def instructors_list(request):
    instructors = Instructors.objects.all()
    return render(request, "instructors.html", {"instructors_list": instructors})

