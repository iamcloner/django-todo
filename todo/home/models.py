from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
