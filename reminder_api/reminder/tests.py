# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from project.models import Project, Environment

def create_project_with_env(name, env_name):
    """Create a project with an environment"""
    project = Project.objects.create(name=name)
    env = project.environments.create(name=env_name)
    return project, env


class ProjectTests(APITestCase):

    def test_stack_create(self):
        """
        Test the stack create interface
        """
        url = reverse("stacks")
        _, env = create_project_with_env("reactive", "staging")

        data = {
            "name": "kafka",
            "logo": "kafka.png",
            "category": "default",
            "reminder": env.reminder.id,
            "urls": [],
            "hosts": []
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('name'), data.get('name'))
        self.assertEqual(response.data.get('logo'), data.get('logo'))
        self.assertEqual(response.data.get('category'), data.get('category'))

    def test_stack_get(self):
        """
        Test the projects get interface
        """
        _, env = create_project_with_env("reactive", "staging")
        stack = env.reminder.stacks.create(
            name="kafka", logo="kafka.png", category="default",
            reminder=env.reminder.id)
        url = '/stacks/%d/' % stack.id

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), stack.name)
        self.assertEqual(response.data.get('logo'), stack.logo)
        self.assertEqual(response.data.get('category'), stack.category)

    def test_stack_list(self):
        """
        Test the stacks list interface
        """
        url = reverse("stacks")
        _, env = create_project_with_env("reactive", "staging")
        stack = env.reminder.stacks.create(
            name="kafka", logo="kafka.png", category="default",
            reminder=env.reminder.id)

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0].get('name'), stack.name)
        self.assertEqual(response.data[0].get('logo'), stack.logo)
        self.assertEqual(response.data[0].get('category'), stack.category)
