# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0020_auto_20170221_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventwinner',
            name='winner_1_college',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='eventwinner',
            name='winner_1_name',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='eventwinner',
            name='winner_2_college',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='eventwinner',
            name='winner_2_name',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='eventwinner',
            name='winner_3_college',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='eventwinner',
            name='winner_3_name',
            field=models.CharField(default=None, max_length=250),
        ),
    ]
