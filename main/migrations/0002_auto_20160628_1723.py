# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 17:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avg_rating',
            name='movie',
        ),
        migrations.DeleteModel(
            name='Avg_Rating',
        ),
    ]
