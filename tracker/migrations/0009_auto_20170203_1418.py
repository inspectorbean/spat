# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_auto_20170203_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='status',
            field=models.CharField(max_length=140),
        ),
    ]
