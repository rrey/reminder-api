# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from inventory import models as inventory_models
from reminder import models as reminder_models


class Project(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return "name: %s" % self.name


class Environment(models.Model):
    project = models.ForeignKey(Project, related_name="environments")
    name = models.CharField(max_length=20)
    inventory = models.ForeignKey(inventory_models.Inventory, blank=True, null=True)
    reminder = models.ForeignKey(reminder_models.Reminder, blank=True, null=True)

    def __str__(self):
        return "name: %s" % self.name
