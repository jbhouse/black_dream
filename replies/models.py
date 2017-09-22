from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from posts.models import Post
User = get_user_model()
from django import template
register = template.Library()

class ReplyManager(models.Manager):
    def create_reply(self, user, post):
        reply = self.create(user = user, post = post)
        return reply

class Reply(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User,related_name='replies')
    created_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, related_name='replies', on_delete=models.CASCADE)
    objects = ReplyManager()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("replies:detail")

    class Meta:
        order_with_respect_to = 'post'
