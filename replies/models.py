from django.db import models
# from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from posts.models import Post
from poetry.models import Poem
from videos.models import Video
User = get_user_model()
from django import template
register = template.Library()

class ReplyManager(models.Manager):
    def create_post_reply(self, user, post):
        reply = self.create(user = user, post = post)
        return reply

    def create_poem_reply(self, user, poem):
        reply = self.create(user = user, poem = poem)
        return reply

class Reply(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User,related_name='replies')
    created_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, blank=True, null=True, related_name='post_replies', on_delete=models.CASCADE)
    poem = models.ForeignKey(Poem, blank=True, null=True, related_name='poem_replies', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, blank=True, null=True, related_name='video_replies', on_delete=models.CASCADE)
    objects = ReplyManager()

    def __str__(self):
        return self.text

    # def get_absolute_url(self):
    #     return reverse("replies:detail")

    class Meta:
        order_with_respect_to = 'post'
