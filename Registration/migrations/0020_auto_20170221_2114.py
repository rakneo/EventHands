# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 15:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Registration', '0019_auto_20170221_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventwinner',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Registration.EventList'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='eventwinner',
            name='user',
        ),
        migrations.AddField(
            model_name='eventwinner',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
