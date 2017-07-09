#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/8 00:47
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : urls.py

from django.conf.urls import url

from apps.problems import api

urlpatterns = [
    # url(r'list/$', api.ProblemsListApi.as_view(), name='problems_list'),
    url(r'^list/$', api.ProblemTempListApi.as_view(), name='problems_list'),
    url(r'^chapters/list/$', api.ChapterTempListApi.as_view(), name='chapters_list')
]