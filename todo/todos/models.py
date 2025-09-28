from django.db import models

from sections.models import TodoSection


class Todo(models.Model):
    section = models.ForeignKey(
        TodoSection, on_delete=models.CASCADE, related_name="sections"
    )
    title = models.CharField(max_length=40)
    description = models.CharField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
