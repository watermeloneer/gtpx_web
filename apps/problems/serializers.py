#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/8 00:21
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : serializers.py


from rest_framework import serializers
from apps.problems.models import Course, Chapter, Problem, ProbelmTemp


class CourseDetailSerializers(serializers.ModelSerializer):
    """课程详情"""

    class Meta:
        model = Course
        fields = ('id', 'name')


class ChapterDetailSerializer(serializers.ModelSerializer):
    """章节详情"""

    course = CourseDetailSerializers()

    class Meta:
        model = Chapter
        fields = ('id', 'name', 'course')


class ProblemDetailSerializer(serializers.ModelSerializer):
    """题目详情页"""

    class Meta:
        model = Problem
        fields = ('id', 'num', 'title', 'choices', 'answers', 'images', 'kind')


class ProblemTempDetailListSerailizer(serializers.ModelSerializer):
    """题目详情列表"""

    choices = serializers.SerializerMethodField('get_choices_list')


    def get_choices_list(self, obj):
        if obj.choices:
            return obj.choices.replace('*', ' ').split()
        else:
            return []

    class Meta:
        model = ProbelmTemp
        fields = ('categoty', 'num', 'title', 'choices', 'answers', 'images', 'radio')