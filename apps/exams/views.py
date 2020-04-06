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
    if not user.has_takein_exam_permission:
        return render(request, 'frontpage.html', {'msg': u'考试次数已用完，请联系管理员--郑先生：18258477953'})

    try:
        exam = Exam.objects.filter(user=user).last()
    except:
        # 没有则创建
        exam = create_exam(request=request)
    if not exam or exam.is_expired or exam.error_str:
        # 过期重新创建
        exam = create_exam(request=request)

    data = {'exam': exam}
    return render(request, 'exam.html', data)



def create_exam(request):
    """创建考试"""

    user = request.user
    # course = user.choices
    course = user.course.num
    # level = int(request.GET.get('level', 1))
    # if course == 11:
    #     level = 0
    # problem_str = gen_problems_str(course=course, level=level)
    problem_str = gen_problems_str(course=course)
    exam = Exam(course=course, problem_str=problem_str, user=user)
    exam.save()
    user.left_exam_count -= 1
    user.save()

    return exam



def gen_problems_str(course, level):
    """产生题目列表"""

    ids_list = ProbelmTemp.objects.filter(course=course, level=level).exclude(category=4).only('pk').values_list('pk', flat=True)
    ids_list = list(ids_list)
    selected_ids = random.sample(ids_list, 100 if len(ids_list) > 100 else len(ids_list) - 5)
    string = ''
    for item in selected_ids:
        string = string + ' ' + str(item)
    return string


@login_required()
def error_view(request):
    """错题集"""
    return render(request, 'error_list.html')