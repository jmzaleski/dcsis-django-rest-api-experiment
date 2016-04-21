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
    url(r'^admin/', admin.site.urls),
    url(r'^$', try_mysql.views.index, name="whattocallit"),
    #url(r'^person?first_name=([a-zA-Z_]+)/$', try_mysql.views.person, name="person_details"),
    url(r'^person/*$', try_mysql.views.person, name="person_details"),
    url(r'^employees/$', views.EmployeeList.as_view()),
    url(r'^employees/(?P<employee_number>[0-9]+)/$', views.EmployeeDetails.as_view()),
    url(r'^apipersons/$', views.LegacyPersonListRestView.as_view()),
    url(r'^apiperson/(?P<first_name>[a-zA-Z]+)/$', views.LegacyPersonDetailsRestView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)