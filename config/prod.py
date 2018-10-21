#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/9 20:24
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : prod.py

# database
# SECURITY WARNING: don't run with debug turned on in production!
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gtpx_db',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'gtpx_db',
#         'USER': 'root',
#         'PASSWORD': 'rootAdmin@123',
#         'HOST': '597378224c91b.gz.cdb.myqcloud.com',
#         'PORT': '5124',
#     }
# }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, 'static/classic/')

MEDIA_ROOT = os.path.join(ROOT_DIR, 'static/upload/')
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(ROOT_DIR, "static"),
    # ("js", os.path.join(STATIC_ROOT, 'js')),
    # ("css", os.path.join(STATIC_ROOT, 'css')),
    # ("images", os.path.join(STATIC_ROOT, 'images')),
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
    'formatters': {
        'standard': {
            'format' : '%(levelname)s [%(asctime)s] [%(name)s:%(module)s:%(funcName)s:%(lineno)s] [%(exc_info)s] %(message)s',
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            #'filters': ['require_debug_false'],
            'filename':os.path.join(ROOT_DIR+'/logs/','access.log'),
            'formatter': 'standard',
            'when': 'midnight',
            'backupCount':30
            },

        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },

    },
    'loggers': {
        'django': {
            'handlers': ['console',],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['file','mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}