#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/8 00:21
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : api.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.problems.admin import ProbelmTempAdmin
from apps.problems.models import ProbelmTemp
from apps.problems.serializers import ProblemTempDetailListSerailizer
from extensions.pagination import StandardResultsSetPagination


class ProblemTempListApi(generics.ListAPIView):
    """题目列表"""
    permission_classes = (IsAuthenticated,)
    serializer_class = ProblemTempDetailListSerailizer
    pagination_class = StandardResultsSetPagination
    queryset = ProbelmTemp.objects.all()
