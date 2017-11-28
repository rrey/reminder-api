# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from inventory import models as inventory_models


class Url(models.Model):
    name = models.URLField()

    def __str__(self):
        return "name: %s" % self.name


class Host(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return "name: %s" % self.name


class StackSection(models.Model):
    name = models.CharField(max_length=20)
    hosts = models.ManyToManyField(Host, blank=True)
    urls = models.ManyToManyField(Url, blank=True)

    def __str__(self):
        return "name: %s" % self.name


class Stack(models.Model):
    name = models.CharField(max_length=20)
    logo = models.ImageField()
    sections = models.ManyToManyField(StackSection, blank=True)

    def __str__(self):
        return "name: %s" % self.name


class Reminder(models.Model):
    name = models.CharField(max_length=20)
    stacks = models.ManyToManyField(Stack, blank=True)

    def __str__(self):
        return "name: %s" % self.name
