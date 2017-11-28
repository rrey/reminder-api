from django.shortcuts import render
from rest_framework import generics

from project.models import Project, Environment
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

    def get_queryset(self):
        project_name = self.kwargs['project_name']
        return Environment.objects.filter(project__name=project_name)

    def perform_create(self, serializer):
        project_name = self.kwargs['project_name']
        project = Project.objects.get(name=project_name)
        serializer.save(project=project)


class EnvironmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentDetailSerializer
    lookup_field = "name"

    def get_queryset(self):
        project_name = self.kwargs['project_name']
        return Environment.objects.filter(project__name=project_name)
