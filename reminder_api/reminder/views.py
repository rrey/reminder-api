from django.shortcuts import render
from rest_framework import generics

from reminder.models import Reminder, Stack, Host, Url
from reminder.serializers import ReminderSerializer, HostSerializer, UrlSerializer
from reminder.serializers import StackDetailSerializer, StackSerializer


class UrlList(generics.ListCreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


class HostList(generics.ListCreateAPIView):
    queryset = Host.objects.all()
    serializer_class = HostSerializer


class StackList(generics.ListCreateAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer

class StackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackDetailSerializer


class ReminderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
