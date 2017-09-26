from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
from django import template
register = template.Library()

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=True)
    details = models.TextField()
    date = models.CharField(max_length=256)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("events:detail", pk=self.pk)

    class Meta:
        ordering = ['created_at']
