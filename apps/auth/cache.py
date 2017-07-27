#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/26 18:05
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : cache.py
from django.conf import settings
from django.core.cache import cache


def cache_session_key_for_request(request):
    """保存用户的session_key"""

    key = "session_%s" % request.user.id
    _session_key = cache.get(key)
    if _session_key:
        cache.delete(_session_key)  # 删除cache中Django产生的session_key
    session_key = request.session.cache_key
    cache.set(key, session_key, settings.SESSION_COOKIE_AGE)