# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from instructors.models import Instructors, InstApply
from django import forms
from django.contrib import messages


def hello(request):
    return render(request, "index.html")

def http(request):
    context = ['value']
    return render(request, "http.html", context)


def hello_python(request, some):
    return HttpResponse("Hello python!!" + some)

def sum_two(request, a, b):
    s = int(a) + int(b)
    return HttpResponse(s)

def instructors_list(request):
    instructors = Instructors.objects.all()
    return render(request, "instructors.html", {"instructors_list": instructors})




class ModelInstApplyForm(forms.ModelForm):
    class Meta:
        model = InstApply
        exclude = ['date_apply', 'comment', 'is_active']



class InstApplyForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    package = forms.ChoiceField(choices=(('standart', 'Standart'),
                                        ('gold', 'Gold'),
                                        ('vip', 'VIP')))
                               # widget=forms.RadioSelect) - випадаюче меню буде стовпчиком без випадань
    new_subscribe = forms.BooleanField()

def inst_apply(request):

    if request.method == "POST":
        form = ModelInstApplyForm(request.POST)
        if form.is_valid():
            form.save()

            # краще писати cleaned_data print(request.POST)
            # замінюємо це на наступний рядок print(form.cleaned_data

            #data = form.cleaned_data видаляємо все закомічене а на його місце пишемо instance=form.save()
            #inst_apply = InstApply()
            #inst_apply.name = data['name']
            #inst_apply.email = data['email']
            #inst_apply.package = data['package']
            #inst_apply.new_subscribe = data['new_subscribe']
            messages.success(request, 'Saved!')


            return redirect('/inst_apply/')
    else:
        form = ModelInstApplyForm(initial={"package": 'gold', "new_subscribe": True})
    return render(request, "inst_apply.html", {'form': form})
    return redirect('forms')


def inst_apply_edit(request, pk):
    instapply = InstApply.objects.get(id=pk)
    form = ModelInstApplyForm(instance=instapply)

    return render(request, "inst_apply_edit.html", {'form': form})


def instapply_delete(request, pk):
    instapply = InstApply.objects.get(id=pk)

    if request.method == "POST":
        instapply.delete()
        messages.success(request, 'Deleted!')
        return redirect('/inst_apply/')

    return render(request, "inst_apply_delete.html", {'inst_apply': instapply})
