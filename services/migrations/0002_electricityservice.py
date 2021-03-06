# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 03:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mlm', '0002_auto_20160430_1253'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricityService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(choices=[('Amaysim', 'Amaysim'), ('Telstra', 'Telstra'), ('Boost', 'Boost'), ('Optus', 'Optus'), ('Vodafone', 'Vodafone')], default='AGL', max_length=64, null=True)),
                ('customer', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mlm.Person')),
            ],
        ),
    ]
