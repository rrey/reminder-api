# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Host(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return "name: %s" % self.name

class Group(models.Model):
    name = models.CharField(max_length=20)
    hosts = models.ManyToManyField(Host, blank=True)

    def __str__(self):
        return "name: %s" % self.name

class Inventory(models.Model):
    name = models.CharField(max_length=20)
    groups = models.ManyToManyField(Group, blank=True)

    def __str__(self):
        return "name: %s" % self.name
