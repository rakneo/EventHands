# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0011_eventlist_event_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventlist',
            name='event_slug',
            field=models.SlugField(default=14, max_length=20),
            preserve_default=False,
        ),
    ]
