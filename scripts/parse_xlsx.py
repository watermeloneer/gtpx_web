#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/8 20:39
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : parse_xlsx.py
import json
import os

from openpyxl import load_workbook

from apps.problems.models import ProbelmTemp, ChapterTemp
from study.settings import BASE_DIR


DATA_DIR = os.path.join(BASE_DIR, 'source_data/xlsx')
def run():
    # print('===========省级电梯管理员==========')
    # parse_left_operater('省级电梯管理员.xlsx', 4)
    # print('===========省级叉车司机==========')
    # parse_left_operater('省级叉车司机.xlsx', 0)
    # print('===========省级叉车管理员==========')
    # parse_left_operater('省级叉车管理员.xlsx', course_id=1)
    # print('============ok===========')
    print('======熔炉省级=====')
    parse_left_operater('锅炉.xlsx', course_id=6)
    print('=======起重机司机===========')
    parse_left_operater('起重机司机.xlsx', course_id=7)
    # print('=======起重机管理员===========')
    # parse_left_operater('起重机管理员.xlsx', course_id=8)

def parse_left_operater(suffix, course_id):
    path = os.path.join(DATA_DIR, suffix)
    wb = load_workbook(path)
    sheet = wb['Sheet1']
    chapters = list()
    print('=======')
    # 章节名去重
    for index, row in enumerate(sheet.rows):
        if index == 0:
            continue
        chapter_name = row[1].value
        if chapter_name:
            if chapter_name not in chapters:
                chapters.append(chapter_name)
                # print(chapters)

    print(chapters)

    # 创建章节
    for index, name in enumerate(chapters):
        c = ChapterTemp(num=index, course=course_id, name=name, level=1)
        print(c.__dict__)
        # print(c.num, c.course, c.name, c.level)
        c.save()


    # 创建题目
    for index, row in enumerate(sheet.rows):
        if index == 0:
            continue
        image = row[6].value
        has_image = row[7].value
        print(has_image)
        print(index)
        # if has_image:
        #     print('====================')
        #     print(type(image))
        #     print(image)
        #     continue
        chapter_name = row[1].value
        chapter = chapters.index(chapter_name)
        course = 4
        num = 0
        title = row[3].value
        choices = row[4].value
        answers = row[5].value
        image = None
        category_name = row[2].value
        if category_name == '单选题':
            category = 0
        elif category_name == '判断题':
            category = 1
        elif category_name == '多选题':
            category = 2
        elif category_name == '图片题':
            category = 3
        else:
            continue

        p = ProbelmTemp(course=course_id, chapter=chapter, num=0, title=title, choices=choices, answers=answers,
                        images=image, category=category, level=1)
        print(p.__dict__)
        # print(p.course, p.chapter, p.num, p.title, p.choices, p.answers, p.images, p.category, p.level)
        # print(index)
        p.save()
    print('====ok====')
