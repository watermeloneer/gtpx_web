# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-09 14:20
from __future__ import unicode_literals

from django.db import migrations, models
import utils.tools


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('account', models.CharField(max_length=30, unique=True, verbose_name='账户')),
                ('name', models.CharField(blank=True, max_length=12, verbose_name='姓名')),
                ('avatar', models.ImageField(blank=True, upload_to=utils.tools.get_file_path, verbose_name='头像')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否活跃')),
                ('is_staff', models.BooleanField(default=False, verbose_name='内部人员')),
                ('choices', models.IntegerField(blank=True, choices=[(0, '叉车'), (1, '其他')], default=0, verbose_name='培训项目')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'db_table': 'users',
                'verbose_name_plural': '用户',
            },
        ),
    ]
