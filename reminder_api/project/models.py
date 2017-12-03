# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return "name: %s" % self.name


class Environment(models.Model):
    name = models.CharField(max_length=20)
    project = models.ForeignKey(Project, related_name="environments")
    reminder = models.ForeignKey('reminder.Reminder')
    inventory = models.ForeignKey('inventory.Inventory')

    class Meta:
        unique_together = ('project', 'name', )

    def __str__(self):
        return "name: %s" % self.name
