# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Reminder(models.Model):
    name = models.CharField(max_length=20)


class Stack(models.Model):
    name = models.CharField(max_length=20, unique=True)
    logo = models.ImageField()
    reminder = models.ForeignKey(Reminder, related_name='stacks')

    class Meta:
        unique_together = ('reminder', 'name', )

    def __str__(self):
        return "name: %s" % self.name


class StackSection(models.Model):
    name = models.CharField(max_length=20, unique=True)
    stack = models.ForeignKey(Stack, related_name='sections')

    def __str__(self):
        return "name: %s" % self.name


class Url(models.Model):
    name = models.URLField()
    section = models.ForeignKey(StackSection, related_name='urls')

    def __str__(self):
        return "name: %s" % self.name


class Host(models.Model):
    name = models.CharField(max_length=20)
    section = models.ForeignKey(StackSection, related_name='hosts')

    def __str__(self):
        return "name: %s" % self.name
