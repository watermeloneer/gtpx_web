#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/7 23:24
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : gen_left_prv_problems.py
import os
import json
from apps.problems.models import ProbelmTemp, ChapterTemp
from study.settings import BASE_DIR

DATA_DIR = os.path.join(BASE_DIR, 'source_data')
def run():
    """更新省级电梯数据"""
    create_chapters()
    create_problems()


def create_chapters():
    path = os.path.join(DATA_DIR, 'left_prv_chapter.json')
    with open(path, 'r', encoding='utf-8') as f:
        for line in json.load(f):
            chapter = ChapterTemp(num=line['num'], course=line['course'], name=line['name'], level=line['level'])
            print(chapter)
            chapter.save()


def create_problems():
    pass
