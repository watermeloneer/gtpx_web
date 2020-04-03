# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170925_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='choices',
            field=models.IntegerField(blank=True, choices=[(0, '叉车司机'), (1, '叉车管理员'), (2, '压力容器操作员'), (3, '压力容器管理员'), (4, '电梯管理员'), (5, '电梯司机'), (6, '熔炉'), (7, '起重机司机'), (8, '起重机管理员'), (9, '安检--低压电工作业'), (10, '安检--高处作业'), (11, '安检--电焊')], default=0, verbose_name='培训项目'),
        ),
    ]