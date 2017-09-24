import datetime

from django.db import models

# Create your models here.
from apps.users.models import User


class Exam(models.Model):
    """考试"""

    # 科目分类
    COURSES_CHOICES = (
        (0, '叉车--叉车司机(N2)'),
        (1, '叉车--场(厂)内专用机动车辆安全管理(A8)'),
        (2, '容器--场固定式压力容器操作(R1)'),
        (3, '容器--锅炉压力容器压力管道安全管理(全部)(A3)'),
        (4, '电梯--安全管理(A4)'),
        (5, '电梯--司机(T3)'),
    )

    # 等级分类
    LEVEL_CHOICES = (
        (0, '全国'),
        (1, '省级')
    )

    course = models.IntegerField('项目', choices=COURSES_CHOICES, default=0)
    level = models.IntegerField('等级', choices=LEVEL_CHOICES, default=0)
    problem_str = models.CharField('题目列表', max_length=2000, blank=True)# 以 " " 连接
    error_str = models.CharField('错题列表', max_length=2000, blank=True, null=True)# 以 " " 连接
    score = models.IntegerField('得分', default=0)
    user = models.ForeignKey(User, verbose_name='相关用户')
    create_time = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'exams'
        verbose_name = verbose_name_plural = '考试'

    @property
    def is_expired(self):
        # 是否过期
        from django.utils import timezone
        return timezone.now() > self.create_time + datetime.timedelta(minutes=60)

    @property
    def get_problems_list(self):
        return [int(problem) for problem in self.problem_str.split()] if self.problem_str else []

    @property
    def get_error_list(self):
        return [int(error) for error in self.error_str.split()] if self.error_str else []



