"""reminder_api URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from project import views as p_views
from reminder import views as r_views

urlpatterns = [
    url(r'^projects/$', p_views.ProjectList.as_view(), name='projects'),
    url(r'^projects/(?P<name>\w+)/$', p_views.ProjectDetail.as_view(),
        name='project_details'),
    url(r'^environments/$', p_views.EnvironmentList.as_view(), name='environments'),
    url(r'^environments/(?P<pk>[0-9]+)/$',
        p_views.EnvironmentDetail.as_view(), name='environment_details'),

    url(r'^reminders/(?P<pk>[0-9]+)/$', r_views.ReminderDetail.as_view()),
    url(r'^stacks/$', r_views.StackList.as_view(), name='stacks'),
    url(r'^stacks/(?P<pk>[0-9]+)/$', r_views.StackDetail.as_view(),
        name='stack_details'),
]

urlpatterns += staticfiles_urlpatterns()
