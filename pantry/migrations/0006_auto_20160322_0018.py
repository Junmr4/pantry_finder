# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantry', '0005_address_raw_coordinate_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='raw_coordinate_data',
            field=models.CharField(blank=True, max_length=4096, null=True),
        ),
    ]
