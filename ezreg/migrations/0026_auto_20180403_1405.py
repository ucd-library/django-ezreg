# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-03 21:05
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezreg', '0025_auto_20170914_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='config',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='event',
            name='ical',
            field=models.FilePathField(blank=True, match=b'*.ics', null=True, path=b'/virtualenvs/django-ezreg/include/ezreg/files'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
