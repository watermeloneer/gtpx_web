#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/9 20:26
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : dev.py

# SECURITY WARNING: don't run with debug turned on in production!
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gtpx_db',
        # 'NAME': 'gtpx',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, 'static/classic/')

MEDIA_ROOT = os.path.join(ROOT_DIR, 'static/upload/')
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(ROOT_DIR, "static"),
    ("js", os.path.join(STATIC_ROOT, 'js')),
    ("css", os.path.join(STATIC_ROOT, 'css')),
    ("images", os.path.join(STATIC_ROOT, 'images')),
)


# cache backend settings
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# sessions settings

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}