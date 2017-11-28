# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from project.models import Project, Environment

class ProjectTests(APITestCase):

    def test_projects_list(self):
        """
        Test the projects list interface
        """
        url = reverse("projects")
        data = {'name': 'test project'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.get().name, 'test project')

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0], data)

    def test_environment_list(self):
        """
        Test the environments list interface
        """
        # {{{ create a project
        url = reverse("projects")
        project_data = {'name': 'test_project'}
        response = self.client.post(url, project_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.get().name, 'test_project')
        # }}}

        url = "/projects/test_project/environments/"
        env_data = {'name': 'staging'}
        response = self.client.post(url, env_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        project = Project.objects.get()
        self.assertEqual(project.environments.count(), 1)
        self.assertEqual(project.environments.get().name, "staging")
