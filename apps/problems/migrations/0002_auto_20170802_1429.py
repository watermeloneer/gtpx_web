# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-02 06:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chaptertemp',
            options={'verbose_name': '知识模块', 'verbose_name_plural': '知识模块'},
        ),
        migrations.AlterModelOptions(
            name='coursetemp',
            options={'verbose_name': '培训项目', 'verbose_name_plural': '培训项目'},
        ),
        migrations.AlterModelOptions(
            name='probelmtemp',
            options={'verbose_name': '题目', 'verbose_name_plural': '题目'},
        ),
    ]
