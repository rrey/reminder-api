# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class BaseModel(models.Model):

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.__dict__)

class Host(BaseModel):
    name = models.CharField(max_length=20)

class Group(BaseModel):
    name = models.CharField(max_length=20)
    hosts = models.ManyToManyField(Host, blank=True)

class Inventory(BaseModel):
    name = models.CharField(max_length=20)
    groups = models.ManyToManyField(Group, blank=True)

class Project(BaseModel):
    name = models.CharField(max_length=20)
    inventory = models.ManyToManyField(Inventory, blank=True)
