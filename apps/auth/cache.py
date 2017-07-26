#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/26 18:05
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : cache.py
from django.conf import settings
from django.contrib.sessions.models import Session
from django.core.cache import cache


def clear_previous_session_of_user(user):
    """单账号登录"""

    key = "session_%s" % user.id
    session_key = cache.get(key)
    if session_key:
        # Session.objects.get(session_key=session_key).delete()
        cache.delete(session_key)# 删除cache中Django产生的session_key


def cache_session_key_for_request(request):
    """保存用户的session_key"""

    key = "session_%s" % request.user.id
    session_key = request.session.cache_key
    cache.set(key, session_key, settings.SESSION_COOKIE_AGE)