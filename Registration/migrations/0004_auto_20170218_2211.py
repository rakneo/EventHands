# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_auto_20170218_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventlist',
            name='thumb_url',
            field=models.CharField(default=' ', max_length=5000),
        ),
        migrations.AlterField(
            model_name='registerdesk',
            name='events_enrolling',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Science Quiz'), ('2', 'Science Model'), ('3', 'Paper Presentation'), ('4', 'Spell bee'), ('5', 'connections'), ('6', 'Poster Painting'), ('7', 'Short Film')], max_length=13),
        ),
    ]
