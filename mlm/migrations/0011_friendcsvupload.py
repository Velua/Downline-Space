# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-15 10:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mlm', '0010_person_postcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendCSVUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendscsvfile', models.FileField(null=True, upload_to=b'', verbose_name='CSV File from PDF')),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mlm.Member')),
            ],
        ),
    ]