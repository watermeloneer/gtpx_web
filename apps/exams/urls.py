#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/8 13:40
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : urls.py
from django.conf.urls import url

from apps.exams import api
from apps.exams.views import exam_view, error_view

urlpatterns = [
    url(r'^$', exam_view, name='exam_index'),
    url(r'^error/$', error_view, name='exam_error'),
    url(r'^upload/$', api.UploadResultsApi.as_view(), name='exam_results_upload'),
    url(r'^problems/list/$', api.ProblemsListApi.as_view(), name='exam_problems_list'),
    url(r'^(?P<pk>\d+)/list/$', api.ExamProblemListApi.as_view(), name='exam_problem_list'),
    url(r'^error/list/$', api.ExamErrorListApi.as_view(), name='exam_error_list'),
]
