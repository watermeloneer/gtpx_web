#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/8 20:39
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : parse_xlsx.py
import json
import os
import traceback

from openpyxl import load_workbook

from apps.problems.models import ProbelmTemp, ChapterTemp
from study.settings import BASE_DIR


DATA_DIR = os.path.join(BASE_DIR, 'source_data/xlsx/2020')

LEVEL = 0  #全国
# LEVEL = 1 # 省级
def run():
    # print('===========省级电梯管理员==========')
    # parse_left_operater('省级电梯管理员.xlsx', 4)
    # print('===========省级叉车司机==========')
    # parse_left_operater('省级叉车司机.xlsx', 0)
    # print('===========省级叉车管理员==========')
    # parse_left_operater('省级叉车管理员.xlsx', course_id=1)
    # print('============ok===========')
    # print('======熔炉省级=====')
    # parse_left_operater('锅炉.xlsx', course_id=6)
    # print('=======起重机司机===========')
    # parse_left_operater('起重机司机.xlsx', course_id=7)
    # print('=======起重机管理员===========')
    """
    |  1 |   0 | 叉车--叉车司机(N2)                                               |
    |  2 |   1 | 叉车--场(厂)内专用机动车辆安全管理(A8)                           |
    |  3 |   2 | 容器--场固定式压力容器操作(R1)                                   |
    |  4 |   3 | '容器--锅炉压力容器压力管道安全管理(全部)(A3)'                   |
    |  5 |   4 | 电梯--安全管理(A4)                                               |
    |  6 |   5 | 电梯--司机(T3)                                                   |
    |  7 |   6 | 熔炉                                                             |
    |  8 |   7 | 起重机司机                                                       |
    |  9 |   8 | 起重机管理员
    |  9 |   12 | 叉车--叉车司机(2020) 
    """

    # parse_left_operater('省级压力容器操作员.xlsx', course_id=2)
    try:
        # parse_left_operater('省级低压电工作业.xlsx', course_id=9)
        # parse_left_operater('省级高处作业.xlsx', course_id=10)
        # parse_left_operater('新电焊国家题库2018.xlsx', course_id=11)
        # parse_left_operater('省级低压电工题库.xlsx', course_id=9)
        # parse_left_operater('2020_01_21特种设备安全管理.xlsx', course_id=12)
        parse_left_operater('观光车总题库.xlsx', course_id=202008)
        parse_left_operater('特种设备安全管理.xlsx', course_id=202007)
        parse_left_operater('一般企业安全负责人.xlsx', course_id=202006)
        parse_left_operater('一般企业安全管理员.xlsx', course_id=202005)
    except :
        traceback.print_exc()

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
        chapter_name = row[0].value # 保持和 L71 一致
        if chapter_name:
            if chapter_name not in chapters:
                chapters.append(chapter_name)
                # print(chapters)

    print(chapters)

    # 创建章节
    for index, name in enumerate(chapters):
        c = ChapterTemp(num=index, course=course_id, name=name, level=LEVEL)
        # print(c.num, c.course, c.name, c.level)
        # FIXME 保存
        c.save()


    # 创建题目
    problem_list = []
    for index, row in enumerate(sheet.rows):
        if index == 0:
            continue
        # FIXME 章节名
        chapter_name = row[0].value
        if not chapter_name:
            break
        chapter = chapters.index(chapter_name)
        # FIXME 题目
        title = row[2].value
        # FIXME 选项
        choices = row[3].value
        # FIXME 答案
        answers = row[4].value
        if not all([title, choices, answers]):
            continue
        image = None
        # FIXME 题目类别
        category_name = row[1].value
        if category_name == '单选题':
            category = 0
        elif category_name == '判断题':
            category = 1
        elif category_name == '多选题':
            category = 2
        elif category_name == '图片题':
            category = 3
        elif category_name == '数字类选择题':
            category = 4
        else:
            continue
        #FIXME 省级level默认为1
        p = ProbelmTemp(course=course_id, chapter=chapter, num=0, title=title, choices=choices, answers=answers,
                        images=image, category=category, level=LEVEL)
        problem_list.append(p)
        print(p.__dict__)
        # print(p.course, p.chapter, p.num, p.title, p.choices, p.answers, p.images, p.category, p.level)
        # print(index)
        # FIXME 保存
        # p.save()
    # print(len(problem_list))
    ProbelmTemp.objects.bulk_create(problem_list, 50)

    print('====ok====')
