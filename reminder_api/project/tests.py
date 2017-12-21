# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from project.models import Project, Environment

class ProjectTests(APITestCase):

    def test_projects_create(self):
        """
        Test the projects list interface
        """
        url = reverse("projects")
        project_name = "reactive"

        data = {'name': project_name}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.get().name, project_name)

    def test_projects_get(self):
        project_name = "reactive"
        project = Project.objects.create(name=project_name)
        url = '/projects/%s/' % project_name

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), project_name)

    def test_projects_list(self):
        project_name = "reactive"
        project = Project.objects.create(name=project_name)
        url = reverse("projects")

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], project_name)
