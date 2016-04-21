"""d3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
import try_mysql.views

from rest_framework.urlpatterns import format_suffix_patterns
from try_rest import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),  # http://127.0.0.1:8000/admin/
    url(r'^$', try_mysql.views.index), # http://127.0.0.1:8000/
    url(r'^persons/$', try_mysql.views.index), # http://127.0.0.1:8000/persons/
    
    #this url turns out weird. http://127.0.0.1:8000/person/first_name/a/?first_name=Mathew
    url(r'^person/first_name/[a-zA-Z]+/$', try_mysql.views.person, name="person_details"),
    
    #I guess I have no idea what i'm doing? 
    url(r'^person/first_name/?(P<first_name>[a-zA-Z]+)/$', try_mysql.views.person2),

    #REST framework works as I guessed it would    
    url(r'^apipersons/$', views.LegacyPersonListRestView.as_view()),
    url(r'^apiperson/?(P<first_name>[a-zA-Z]+)/$', views.LegacyPersonDetailsRestView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)