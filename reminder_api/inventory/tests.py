# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from inventory.models import Project

class ReminderTests(APITestCase):

    def test_create_project(self):
        """
        Ensure we can create a new project object.
        """
        url = "/projects"
        data = {'name': 'test project'}
        response = self.client.post(url, data, format='json')
        print response.data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.get().name, 'test project')
