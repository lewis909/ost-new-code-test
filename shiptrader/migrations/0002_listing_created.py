# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-13 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shiptrader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]