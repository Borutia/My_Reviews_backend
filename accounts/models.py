from django.db import models

from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=128
    )
    email = models.EmailField(
        required=True,
        #validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = models.CharField(
        min_length=6
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )
    updated = models.DateTimeField(
        auto_now_add=False,
        auto_now=True
    )

    def __str__(self):
        return "User %d" % self.id

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

