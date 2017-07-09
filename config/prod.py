#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/9 20:24
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : prod.py

# database
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gtpx_db',
        'USER': 'root',
        'PASSWORD': 'password123/',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
