from django.db import models
from django.contrib.auth.models import User


class Color(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=6)


class TodoSection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    title = models.CharField(max_length=40)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)
    color = models.ForeignKey(
        Color, on_delete=models.SET_NULL, null=True, related_name="tcolor"
    )
