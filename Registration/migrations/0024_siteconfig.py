# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0023_eventlist_event_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(default='EMT', max_length=300)),
            ],
        ),
    ]