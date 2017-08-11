#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/8 12:47
# @Author  : 赵在化
# @email  : zaihuazhao@163.com
# @File    : api.py
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.exams.models import Exam
from apps.problems.models import ProbelmTemp
from apps.problems.serializers import ProblemExamListSerializer
from extensions.pagination import StandardResultsSetPagination


class ExamProblemListApi(generics.ListAPIView):
    """考试题目列表"""

    permission_classes = (IsAuthenticated,)
    serializer_class = ProblemExamListSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        pk = self.kwargs['pk']
        exam = get_object_or_404(Exam, pk=pk)
        ids_list = exam.problem_str.split()
        return ProbelmTemp.objects.filter(id__in=ids_list)


class UploadResultsApi(APIView):
    """上传考试结果"""

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        error_list = self.request.data.get('error_list', [])
        rightcount = int(self.request.data.get('rightcount', 0))
        score = rightcount
        error_str = ''
        for error in error_list:
            error_str = error_str + ' ' + str(error)

        data = {'error_str': error_str, 'score': score}
        exam = Exam.objects.filter(user=request.user).last()
        exam.error_str = error_str
        exam.score = score
        exam.save()

        return Response(data=data, status=status.HTTP_200_OK)

    # def patch(self, request, pk):
    #     errot_list = self.request.data.get('errot_list', [])
    #     score = 100 - len(errot_list)
    #     error_str = ''
    #     for error in errot_list:
    #         error_str = error_str + ' ' + str(error)
    #     data = {'error_str': error_str, 'score': score}
    #     queryset = Exam.objects.filter(pk=pk)
    #     if not queryset:
    #         exp = APIException('不存在的考试id：%s' % pk)
    #         exp.status_code = status.HTTP_404_NOT_FOUND
    #         raise exp
    #     queryset.update(**data)
    #     return Response(data=data, status=status.HTTP_200_OK)

        # 此处不适用serialize是因为下面会更新所有的字段值
        # # pk = request.kwargs['exam_id']
        # exam = get_object_or_404(Exam, pk=pk)
        # serializer = ExamPatchSerializer(exam, data=data, partial=False)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(data=serializer.data, status=status.HTTP_200_OK)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProblemsListApi(APIView):
    """考试题目"""

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        exam = Exam.objects.filter(user=request.user).last()
        return Response(data=exam.get_problems_list, status=status.HTTP_200_OK)