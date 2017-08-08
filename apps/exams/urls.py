#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/8 13:40
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : urls.py
from django.conf.urls import url

from apps.exams.views import exam_view

urlpatterns = [
    url(r'^$', exam_view, name='exam_index'),
]
