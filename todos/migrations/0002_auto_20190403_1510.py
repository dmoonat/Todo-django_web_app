# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-03 09:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='schedule',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
