# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 00:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('add_plan_app', '0004_auto_20161024_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='travelenddate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='plan',
            name='travelstartdate',
            field=models.DateField(),
        ),
    ]
