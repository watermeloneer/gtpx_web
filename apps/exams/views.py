import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.exams.models import Exam
from apps.problems.models import ProbelmTemp


@login_required
def exam_view(request):
    """考试界面"""
    # 查看已有的考试是否有正在考试 ->返回当前考试
    #                        ->创建考试题目
    #                        -> 返回考试题目接口
    #
    user = request.user
    try:
        exam = Exam.objects.filter(user=user).last()
    except:
        # 没有则创建
        exam = create_exam(request=request)
    if not exam or exam.is_expired:
        # 过期重新创建
        exam = create_exam(request=request)

    data = {'exam': exam}
    return render(request, 'exam.html', data)



def create_exam(request):
    """创建考试"""

    user = request.user
    course = user.choices
    level = int(request.GET.get('level', 1))
    problem_str = gen_problems_str(course=course, level=level)
    exam = Exam(course=course, level=level, problem_str=problem_str, user=user)
    exam.save()

    return exam



def gen_problems_str(course, level):
    """产生题目列表"""

    ids_list = ProbelmTemp.objects.filter(course=course, level=level).only('pk').values_list('pk', flat=True)
    ids_list = list(ids_list)
    selected_ids = random.sample(ids_list, 100)
    string = ''
    for item in selected_ids:
        string = string + ' ' + str(item)
    return string