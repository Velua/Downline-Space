# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-08 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20160508_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='electricityservice',
            name='kwh',
            field=models.FloatField(blank=True, default=0.5, null=True),
        ),
    ]
