# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20170202_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finance',
            name='yr_contract_value',
        ),
        migrations.AlterField(
            model_name='finance',
            name='contract_end',
            field=models.DateField(blank=True, null=True),
        ),
    ]