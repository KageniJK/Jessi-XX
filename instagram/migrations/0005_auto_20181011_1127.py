# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-11 08:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_auto_20181009_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='image',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='instagram.Image'),
        ),
    ]
