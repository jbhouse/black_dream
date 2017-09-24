from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
from django import template
register = template.Library()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256,unique=True)
    created_at = models.DateTimeField(auto_now=True)
    details = models.TextField()

    def __str__(self):
        return self.title

    def reply_count(self):
        post = Post.objects.prefetch_related('post_replies').get(id=self.pk)
        return post.post_replies.all().count()

    # def get_absolute_url(self):
    #     return reverse("posts:detail", pk=self.pk)

    class Meta:
        ordering = ['created_at']
