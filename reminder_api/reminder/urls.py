from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\w+)/$', views.ReminderDetail.as_view()),
]
