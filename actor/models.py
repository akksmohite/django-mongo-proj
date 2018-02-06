from __future__ import unicode_literals
from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    film = models.CharField(max_length=255)

