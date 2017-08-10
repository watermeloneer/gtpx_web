#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/8 12:46
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : serializers.py

from rest_framework import serializers

from apps.exams.models import Exam


class ExamPatchSerializer(serializers.ModelSerializer):
    """修改考试结果"""

    class Meta:
        model = Exam
        fields = ('error_str', 'score')