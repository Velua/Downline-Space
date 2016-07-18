# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 02:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mlm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobileService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(choices=[('Amaysim', 'Amaysim'), ('Telstra', 'Telstra'), ('Boost', 'Boost'), ('Optus', 'Optus'), ('Vodafone', 'Vodafone')], default='Telstra', max_length=32, null=True)),
                ('phone', models.CharField(choices=[('HTC', 'HTC'), ('Samsung', 'Samsung'), ('iPhone', 'iPhone')], default='iPhone', max_length=32, null=True)),
                ('servicetype', models.CharField(choices=[('Plan', 'Plan'), ('Prepaid', 'Prepaid')], default='', max_length=32, null=True)),
                ('monthlycost', models.FloatField(default=80, null=True)),
                ('expiry', models.DateField(null=True)),
                ('customer', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mlm.Person')),
            ],
        ),
    ]
