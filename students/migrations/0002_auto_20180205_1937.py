# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-05 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='date_of_birth',
            field=models.DateField(blank=True),
        ),
    ]