from django.db import models

# Create your models here.

class Course(models.Model):
    """课程分类"""

    name = models.CharField('课程名称', max_length=100, blank=True)

    class Meta:
        db_table = 'courses'
        verbose_name = verbose_name_plural = '课程分类'

    def __str__(self):
        return self.name



class Chapter(models.Model):
    """章节"""

    name = models.CharField('章节名称', max_length=100, blank=True)
    course = models.ForeignKey(Course, verbose_name='课程分类')

    class Meta:
        db_table = 'chapters'
        verbose_name = verbose_name_plural = '章节名称'

    def __str__(self):
        return self.name



class Problem(models.Model):
    """问题模型"""

    num = models.IntegerField('序号', blank=True, null=True)
    title = models.CharField('标题', max_length=200, blank=True)
    choices = models.CharField('选择内容', max_length=500, blank=True)
    answers = models.CharField('答案', max_length=20, blank=True)
    images = models.CharField('图片', max_length=200, blank=True)
    kind = models.IntegerField('题目类型', default=1)
    chapter = models.ForeignKey(Chapter, verbose_name='所属章节')
    course = models.ForeignKey(Course, verbose_name='所属课程')

    class Meta:
        db_table = 'problems'
        verbose_name = verbose_name_plural = '题目'

    def __str__(self):
        return self.title