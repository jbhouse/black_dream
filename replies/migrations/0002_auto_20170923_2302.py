# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 23:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poetry', '0001_initial'),
        ('replies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='poem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poem_replies', to='poetry.Poem'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_replies', to='posts.Post'),
        ),
    ]