from datetime import datetime

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
from utils.tools import get_file_path


class MyUserManager(BaseUserManager):
    def create_user(self, account, password=None, **extra_fields):
        """
        创建一个用户，账号，和密码
        """
        now = datetime.now()
        if not account:
            raise ValueError('必须填写账号')
        user = self.model(account=account, create_time=now, update_time=now, **extra_fields)
        user.set_password(password) # 会不存原始的密码
        user.save(using=self._db)
        return user

    def create_superuser(self, account, password, **extra_fields):
        """
        创建一个超级用户
        """
        u = self.create_user(account=account, password=password, **extra_fields)
        u.is_staff = True
        u.is_superuser = True
        u.save(using=self._db)
        return u


class User(AbstractBaseUser, PermissionsMixin):
    """user model"""
    CHOICES_TYPE = (
        (0, '叉车--叉车司机(N2)'),
        (1, '叉车--场(厂)内专用机动车辆安全管理(A8)'),
        (2, '容器--场固定式压力容器操作(R1)'),
        (3, '容器--锅炉压力容器压力管道安全管理(全部)(A3)'),
    )
    account = models.CharField('账户', max_length=30, unique=True)
    name = models.CharField('姓名', max_length=12, blank=True)
    avatar = models.ImageField('头像', upload_to=get_file_path, max_length=100, blank=True)
    create_time = models.DateTimeField('注册时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    is_active = models.BooleanField('是否活跃', default=True)
    is_staff = models.BooleanField('内部人员', default=False)
    choices = models.IntegerField('培训项目', default=0, choices=CHOICES_TYPE, blank=True)  # 0表示叉车 1表示其他

    # 代表用户名字段
    USERNAME_FIELD = 'account'

    objects = MyUserManager()

    class Meta:
        db_table = 'users'
        verbose_name = verbose_name_plural = '用户'

    def get_full_name(self):
        return self.account

    def get_short_name(self):
        return self.account

    def get_choices(self):
        return

    def __str__(self):
        return self.account

    def save(self, *args, **kwargs):
        if not len(self.password) == 32:# 设置密码
            self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

