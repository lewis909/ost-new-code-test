# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-13 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shiptrader', '0002_listing_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='activite',
            field=models.BooleanField(default=True),
        ),
    ]