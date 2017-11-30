# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Inventory(models.Model):
    name = models.CharField(max_length=20)


class Group(models.Model):
    name = models.CharField(max_length=20)
    inventory = models.ForeignKey(Inventory, related_name='groups')

    def __str__(self):
        return "name: %s" % self.name


class Host(models.Model):
    name = models.CharField(max_length=20)
    group = models.ForeignKey(Group, related_name='hosts')

    def __str__(self):
        return "name: %s" % self.name
