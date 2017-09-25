# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 04:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_auto_20170925_0457'),
        ('replies', '0002_auto_20170923_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_replies', to='videos.Video'),
        ),
    ]