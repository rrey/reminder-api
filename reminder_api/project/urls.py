from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProjectList.as_view(), name='projects'),
    url(r'^(?P<name>\w+)/$', views.ProjectDetail.as_view()),
    url(r'^(?P<project_name>\w+)/environments/$', views.EnvironmentList.as_view(), name="environments"),
    url(r'^(?P<project_name>\w+)/environments/(?P<name>\w+)/$', views.EnvironmentDetail.as_view()),
]
