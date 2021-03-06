# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('events', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterDesk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cand_name', models.CharField(max_length=250)),
                ('cand_dept', models.CharField(max_length=150)),
                ('cand_college', models.CharField(max_length=250)),
                ('event_part', models.ManyToManyField(to='Registration.EventList')),
            ],
        ),
    ]
