# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-08 05:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='subject',
            new_name='course',
        ),
    ]
