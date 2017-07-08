#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/8 22:54
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : pagination.py
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1000