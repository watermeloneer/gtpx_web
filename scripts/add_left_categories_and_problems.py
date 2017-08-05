#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/5 18:03
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : add_left_categories_and_problems.py
import os
import json
from apps.problems.models import ChapterTemp, ProbelmTemp
from study.settings import BASE_DIR

DATA_DIR = os.path.join(BASE_DIR, 'source_data')

def run():
    """新增电梯培训项目"""

    create_chapters()
    create_problems()


def create_chapters():
    """导入章节数据"""

    path = os.path.join(DATA_DIR, 'category_left.txt')
    with open(path, 'r') as f:
        data = json.load(f)
        for line in data:
            chapter = ChapterTemp(num=line['num'], course=line['group'], name=line['name'] )
            print(chapter)
            chapter.save()


def create_problems():
    """导入题目"""

    path = os.path.join(DATA_DIR, 'problems_left.txt')
    with open(path, 'r') as f:
        data = json.load(f)
        for line in data:
            # print(line)
            # {'images': '', 'num': '47', 'categoty': 4, 'choices': '**A、法律**B、行政法规**C、安全技术规范**D、标准。**', 'group': 5, 'radio': 0, 'answers': 'A', 'title': '48、《中华人民共和国特种设备安全法》是全国人大颁布的（\u3000\u3000）。(单选题)'}
            problem = ProbelmTemp(course=line['group'], chapter=line['categoty'], num=line['num'], title=line['title'],
                                  choices=line['choices'], answers=line['answers'], images=line['images'], category=line['radio'])
            print(problem)
            problem.save()