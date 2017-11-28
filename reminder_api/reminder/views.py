from django.shortcuts import render
from rest_framework import generics

from reminder.models import Reminder, Stack, StackSection, Host, Url
from reminder.serializers import ReminderSerializer, StackSerializer, StackSectionSerializer, HostSerializer, UrlSerializer


class UrlList(generics.ListCreateAPIView):
    serializer_class = UrlSerializer

    def get_queryset(self):
        stacksection_name = self.kwargs['stacksection_name']
        return Url.objects.filter(stacksection__name=stacksection_name)


class HostList(generics.ListCreateAPIView):
    serializer_class = HostSerializer

    def get_queryset(self):
        stacksection_name = self.kwargs['stacksection_name']
        return Host.objects.filter(stacksection__name=stacksection_name)


class StackSectionList(generics.ListCreateAPIView):
    serializer_class = StackSectionSerializer

    def get_queryset(self):
        stack_name = self.kwargs['stack_name']
        return StackSection.objects.filter(stack__name=stack_name)


class StackList(generics.ListCreateAPIView):
    serializer_class = StackSerializer

    def get_queryset(self):
        reminder_name = self.kwargs['reminder_name']
        return Stack.objects.filter(reminder__name=reminder_name)


class ReminderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer


class ReminderList(generics.ListCreateAPIView):
    serializer_class = ReminderSerializer

    def get_queryset(self):
        project_name = self.kwargs['project_name']
        return Reminder.objects.filter(project__name=project_name)
