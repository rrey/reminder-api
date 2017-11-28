from django.shortcuts import render

from inventory.models import Inventory, Group, Host
from inventory.serializers import InventorySerializer, GroupSerializer, HostSerializer
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework import generics


class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class HostList(generics.ListCreateAPIView):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
