# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mlm', '0005_auto_20160501_1615'),
        ('services', '0004_auto_20160507_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='BroadbandService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(choices=[('Optus', 'Optus'), ('Westnet', 'Westnet'), ('Telstra', 'Telstra')], default='Telstra', max_length=64, null=True)),
                ('expiry', models.DateField(null=True)),
                ('GBpermonth', models.IntegerField(blank=True, null=True)),
                ('connectiontype', models.CharField(blank=True, choices=[('ADSL 2+', 'ADSL 2+'), ('NBN', 'NBN'), ('ADSL', 'ADSL')], max_length=64, null=True)),
                ('customer', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mlm.Person')),
            ],
        ),
    ]
