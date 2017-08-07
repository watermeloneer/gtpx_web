#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/8 00:21
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : api.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.problems.admin import ProbelmTempAdmin
from apps.problems.models import ProbelmTemp, ChapterTemp
from apps.problems.serializers import ProblemTempDetailListSerailizer, ChapterTempListSerializer
from extensions.pagination import StandardResultsSetPagination


class ProblemTempListApi(generics.ListAPIView):
    """题目列表"""
    permission_classes = (IsAuthenticated,)
    serializer_class = ProblemTempDetailListSerailizer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        course = self.request.user.choices
        chapter = int(self.request.query_params.get('chapter', 0))
        category = self.request.query_params.get('category')
        level = int(self.request.query_params.get('level', 0))
        filer_params = {'course': course, 'chapter': chapter, 'level': level}
        if category:
            filer_params['category'] = int(category)

        return ProbelmTemp.objects.filter(**filer_params).order_by('id')


class ChapterTempListApi(generics.ListAPIView):
    """章节列表"""

    permission_classes = (IsAuthenticated,)
    serializer_class = ChapterTempListSerializer

    def get_queryset(self):
        course = self.request.user.choices
        level = int(self.request.query_params.get('level', 0))
        return ChapterTemp.objects.filter(course=course, level=level).order_by('id')
