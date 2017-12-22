# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from project.models import Project, Environment

class ProjectTests(APITestCase):

    def test_projects_create(self):
        """
        Test the projects create interface
        """
        url = reverse("projects")
        project_name = "reactive"

        data = {'name': project_name}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('name'), project_name)

    def test_projects_get(self):
        """
        Test the projects get interface
        """
        project_name = "reactive"
        project = Project.objects.create(name=project_name)
        url = '/projects/%s/' % project_name

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), project_name)

    def test_projects_list(self):
        """
        Test the projects list interface
        """
        project_name = "reactive"
        project = Project.objects.create(name=project_name)
        url = reverse("projects")

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], project_name)

    def test_environement_create(self):
        """
        Test the environment create interface
        """
        url = reverse("environments")
        project_name = "reactive"
        env_name = "staging"
        project = Project.objects.create(name=project_name)

        data = {'project': project.id, 'name': env_name}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('name'), env_name)

    def test_environments_get(self):
        """
        Test the environments get interface
        """
        project_name = "reactive"
        env_name = "staging"
        project = Project.objects.create(name=project_name)
        env = project.environments.create(name=env_name)
        url = '/environments/%d/' % env.id

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), env_name)

    def test_environement_list(self):
        """
        Test the environment list interface
        """
        url = reverse("environments")
        project_name = "reactive"
        env_name = "staging"
        project = Project.objects.create(name=project_name)
        env = project.environments.create(name=env_name)

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], env_name)
