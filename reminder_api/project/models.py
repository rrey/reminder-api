# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from reminder.models import Reminder
from inventory.models import Inventory


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

    def save(self, *args, **kwargs):
        if not self.pk:
            self.reminder = Reminder.objects.create()
            self.inventory = Inventory.objects.create()
        super(Environment, self).save(*args, **kwargs)

    def __str__(self):
        return "name: %s" % self.name
