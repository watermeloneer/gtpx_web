from django.db import models


# Create your models here.

# class Course(models.Model):
#     """项目"""
#
#     name = models.CharField('项目名称', max_length=100, blank=True)
#
#     class Meta:
#         db_table = 'courses'
#         verbose_name = verbose_name_plural = '项目'
#
#     def __str__(self):
#         return self.name
#
#
#
# class Chapter(models.Model):
#     """知识模块"""
#
#     name = models.CharField('知识模块', max_length=100, blank=True)
#     course = models.ForeignKey(Course, verbose_name='项目')
#
#     class Meta:
#         db_table = 'chapters'
#         verbose_name = verbose_name_plural = '知识模块'
#
#     def __str__(self):
#         return self.name
#
#
#
# class Problem(models.Model):
#     """问题模型"""
#
#     num = models.IntegerField('序号', blank=True, null=True)
#     title = models.CharField('标题', max_length=200, blank=True)
#     choices = models.CharField('选择内容', max_length=500, blank=True)
#     answers = models.CharField('答案', max_length=20, blank=True)
#     images = models.CharField('图片', max_length=200, blank=True)
#     kind = models.IntegerField('题目类型', default=1)
#     chapter = models.ForeignKey(Chapter, verbose_name='所属知识模块')
#     course = models.ForeignKey(Course, verbose_name='所属项目')
#
#     class Meta:
#         db_table = 'problems'
#         verbose_name = verbose_name_plural = '题目'
#
#     def __str__(self):
#         return self.title


class ProbelmTemp(models.Model):
    # {
    #     "group": 0,
    #     "categoty": 0,
    #     "title": "2、根据以下现象选择正确的观点？(单选题)",
    #     "answers": "A",
    #     "choices": "**A、车入车库需手动开门**B、车辆检修需停稳**C、检修时，叉齿需降至地面**D、检修需关闭发动机**",
    #     "num": "1",
    #     "radio": 0,
    #     "images": "yhpicture/nj_cz_t2_tp97.jpg"
    # }
    CATEGORY_TYPES = (
        (0, '单选题'),
        (1, '判断题'),
        (2, '多选题'),
        (3, '图片题'),
    )
    course = models.IntegerField('所属课程id')
    chapter = models.IntegerField('所属章节id')
    num = models.IntegerField('序号', blank=True, null=True)
    title = models.CharField('标题', max_length=200, blank=True)
    choices = models.CharField('选择内容', max_length=500, blank=True)
    answers = models.CharField('答案', max_length=20, blank=True)
    images = models.ImageField('图片', upload_to='yhpicture', max_length=200, blank=True)
    category = models.IntegerField('题目类型', choices=CATEGORY_TYPES, default=0)

    class Meta:
        db_table = 'problem_temp'
        verbose_name = verbose_name_plural = '题目(未处理)'

    def __str__(self):
        return '项目:%s 知识模块:%s 记录:%s' % (self.course, self.chapter, self.title)


class CategoryTemp(models.Model):
    # {
    #     "num": 10,
    #     "group": 0,
    #     "name": "返回大纲明细"
    # }

    num = models.IntegerField('知识模块id')
    group = models.IntegerField('所属项目num')
    name = models.CharField('知识模块', max_length=100)

    class Meta:
        db_table = 'category_temp'
        verbose_name = verbose_name_plural = '知识模块(未处理)'

    def __str__(self):
        return '项目:%s 记录:%s：%s' % (self.group, self.num, self.name)


class CourseTemp(models.Model):
    num = models.IntegerField('项目id')
    name = models.CharField('项目名称', max_length=100)

    class Meta:
        db_table = 'course_temp'
        verbose_name = verbose_name_plural = '项目(未处理)'

    def __str__(self):
        return '%s：%s' % (self.num, self.name)
