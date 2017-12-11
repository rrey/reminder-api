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


class Url(models.Model):
    url = models.URLField()
    stack = models.ForeignKey(Stack, related_name='urls')

    def __str__(self):
        return "url: %s" % self.url


class Host(models.Model):
    hostname = models.CharField(max_length=50)
    stack = models.ForeignKey(Stack, related_name='hosts')

    def __str__(self):
        return "hostname: %s" % self.hostname
