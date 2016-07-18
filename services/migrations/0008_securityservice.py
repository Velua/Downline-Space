# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-08 01:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mlm', '0005_auto_20160501_1615'),
        ('services', '0007_electricityservice_kwh'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interestedinsecuringhome', models.BooleanField()),
                ('provider', models.CharField(blank=True, max_length=64, null=True)),
                ('monthlycost', models.FloatField(blank=True, default=80, null=True)),
                ('expiry', models.DateField(blank=True, null=True)),
                ('customer', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mlm.Person')),
            ],
        ),
    ]