# -*- encoding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.html import strip_tags


def login(request):
    """登录模块"""

    if request.method=='GET':
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('admin:index'))
        else:
            return render(request, 'index.html')
    elif request.method=='POST':
        """登录"""
        account = strip_tags(request.POST.get('account', '').lower().strip())
        password = request.POST.get('password', '').strip()
        if not account or not password:
            data = {"msg": '请输入账户名或密码'}
            return render(request, 'index.html', data)
        user = authenticate(username=account, password=password)
        if user:
            auth.login(request=request, user=user)
            if user.is_superuser:
                """管理员账户"""
                return HttpResponseRedirect('/admin')
                # return render(request, 'index.html')
            else:
                """普通账户"""
                return render(request, 'index.html')
        else:
            data = {"msg": '账户或密码错误'}
            return render(request, 'index.html', data)
    else:
        return HttpResponseRedirect(reverse('index'))