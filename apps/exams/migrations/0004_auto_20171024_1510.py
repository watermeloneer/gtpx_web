# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-24 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_auto_20170808_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='error_str',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='错题列表'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='problem_str',
            field=models.CharField(blank=True, max_length=2000, verbose_name='题目列表'),
        ),
    ]
