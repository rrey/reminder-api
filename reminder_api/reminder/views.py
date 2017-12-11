from django.shortcuts import render
from rest_framework import generics

from reminder.models import Reminder, Stack, Host, Url
from reminder.serializers import ReminderSerializer, HostSerializer, UrlSerializer
from reminder.serializers import StackDetailSerializer 


class UrlList(generics.ListCreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


class HostList(generics.ListCreateAPIView):
    queryset = Host.objects.all()
    serializer_class = HostSerializer


class StackList(generics.ListCreateAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackDetailSerializer

    def perform_create(self, serializer):
        reminder_id = self.request.data.get('reminder')
        reminder = Reminder.objects.get(id=reminder_id)
        serializer.save(reminder=reminder)

class StackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackDetailSerializer


class ReminderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
