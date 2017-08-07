#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/8 00:21
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : serializers.py


from rest_framework import serializers
from apps.problems.models import ProbelmTemp, ChapterTemp, CourseTemp




class ProblemTempDetailListSerailizer(serializers.ModelSerializer):
    """题目详情列表"""

    choices = serializers.SerializerMethodField('get_choices_list')
    category = serializers.SerializerMethodField('get_category_doc')
    course = serializers.SerializerMethodField('get_course_doc')
    chapter = serializers.SerializerMethodField('get_chapter_doc')

    def get_choices_list(self, obj):
        if obj.choices:
            return obj.choices.replace('*', ' ').split()
        else:
            return []

    def get_category_doc(self, obj):
        return obj.get_category_display()

    def get_course_doc(self, obj):
        return CourseTemp.objects.get(num=obj.course).name

    def get_chapter_doc(self, obj):
        return ChapterTemp.objects.get(num=obj.chapter, course=obj.course).name

    class Meta:
        model = ProbelmTemp
        fields = ('course', 'chapter', 'title', 'choices', 'answers', 'images', 'category')


class ChapterTempListSerializer(serializers.ModelSerializer):
    """章节列表"""

    class Meta:
        model = ChapterTemp
        fields = ('num', 'name')