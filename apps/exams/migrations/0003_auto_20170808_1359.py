# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-08 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_auto_20170808_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='error_str',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='错题列表'),
        ),
    ]
