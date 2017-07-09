#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/9 20:26
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : dev.py

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gtpx_db',
        # 'NAME': 'gtpx',
        'USER': 'root',
        'PASSWORD': 'Password123/',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}