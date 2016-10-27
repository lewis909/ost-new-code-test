# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-16 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Starship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starship_class', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('length', models.FloatField()),
                ('hyperdrive_rating', models.FloatField()),
                ('cargo_capacity', models.BigIntegerField()),
                ('crew', models.IntegerField()),
                ('passengers', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='ship_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='shiptrader.Starship'),
        ),
    ]
