# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0012_eventlist_event_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlist',
            name='event_slug',
            field=models.SlugField(default=0, max_length=20),
        ),
    ]
