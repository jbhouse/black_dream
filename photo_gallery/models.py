from django.db import models
from django import template
register = template.Library()
# Create your models here.

class Photo(models.Model):
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    source = models.TextField()

    def __str__(self):
        return self.description
