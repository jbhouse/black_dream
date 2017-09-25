from django.db import models
from embed_video.fields import EmbedVideoField

class Video(models.Model):
    video = EmbedVideoField()
    created_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=80, default='Click for more')
