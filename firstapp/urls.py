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
from django.http import HttpResponse
from django.shortcuts import render

#from django.conf import settings
#def some_view(request):
    # ...
    #return render_to_response('my_template.html',
                             # my_data_dictionary,
                              #context_instance=RequestContext(request))

def hello(request):
    return render(request, "index.html")

def http(request):
    return render(request, "http.html")


def hello_python(request, some):
    return HttpResponse("Hello python!!" + some)

def sum_two(request, a, b):
    s = int(a) + int(b)
    return HttpResponse(s)


urlpatterns = [
    url(r'^$', hello, name='home'),
    url(r'^python/(?P<some>\w+)$', hello_python),
    url(r'^http/$', http),
    url(r'^sum/(?P<a>\d+)/(?P<b>\d+)$', sum_two),
    url(r'^admin/', admin.site.urls),
]
