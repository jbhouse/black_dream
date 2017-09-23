from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
from django import template
register = template.Library()

# Create your models here.
class Poem(models.Model):
    title = models.CharField(max_length=256,unique=True)
    created_at = models.DateTimeField(auto_now=True)
    details = models.TextField()

    def __str__(self):
        return self.title

    def reply_count(self):
        poem = Poem.objects.prefetch_related('poem_replies').get(id=self.pk)
        return poem.replies.all().count()

    def get_absolute_url(self):
        return reverse("poems:detail", pk=self.pk)

    class Meta:
        ordering = ['created_at']
