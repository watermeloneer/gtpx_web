#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/8 00:21
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : api.py

from rest_framework import generics

from apps.problems.models import Problem
from apps.problems.serializers import ProblemDetailSerializer


class ProblemsListApi(generics.ListAPIView):
    """题目列表"""

    serializer_class = ProblemDetailSerializer
    queryset = Problem.objects.all()

