from django.shortcuts import render
from rest_framework import generics

from project.models import Project, Environment
from reminder.models import Reminder
from inventory.models import Inventory

from project.serializers import ProjectSerializer, ProjectDetailSerializer
from project.serializers import EnvironmentSerializer, EnvironmentDetailSerializer


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    lookup_field = "name"


class EnvironmentList(generics.ListCreateAPIView):
    serializer_class = EnvironmentSerializer
    queryset = Environment.objects.all()

    def perform_create(self, serializer):
        project_id = self.request.data.get('project')
        project = Project.objects.get(id=project_id)
        reminder = Reminder.objects.create()
        inventory = Inventory.objects.create()
        serializer.save(project=project, reminder=reminder, inventory=inventory)


class EnvironmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentDetailSerializer
