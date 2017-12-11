from django.shortcuts import render
from rest_framework import generics

from reminder.models import Reminder, Stack, StackSection, Host, Url
from reminder.serializers import ReminderSerializer, StackSerializer, StackSectionSerializer, HostSerializer, UrlSerializer
from reminder.serializers import StackDetailSerializer, StackSectionDetailSerializer


class UrlList(generics.ListCreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


class HostList(generics.ListCreateAPIView):
    queryset = Host.objects.all()
    serializer_class = HostSerializer


class StackSectionList(generics.ListCreateAPIView):
    queryset = StackSection.objects.all()
    serializer_class = StackSectionSerializer

class StackSectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StackSection.objects.all()
    serializer_class = StackSectionDetailSerializer


class StackList(generics.ListCreateAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer

class StackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackDetailSerializer


class ReminderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
