"""firstapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from instructors.views import hello, hello_python, http, sum_two, instructors_list, inst_apply, instapply_edit, instapply_delete
from courses.views import courses_list
from courses.views import main_page
from courses.views import forms





urlpatterns = [
    url(r'^$', hello, name='home'),
    url(r'^main_page/$', main_page),
    url(r'^forms/$', forms),
    url(r'^inst_apply/$', inst_apply),

    url(r'^inst_apply/(?P<pk>\d+)/edit/$', instapply_edit),
    url(r'^inst_apply/(?P<pk>\d+)/delete/$', instapply_delete),
    url(r'^python/$', hello_python),
    url(r'^http/$', http),
    url(r'^sum/(?P<a>\d+)/(?P<b>\d+)$', sum_two),
    url(r'^instructors/$', instructors_list),
    url(r'^courses/$', courses_list),
    url(r'^admin/', admin.site.urls),
]
