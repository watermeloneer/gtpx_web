# -*- encoding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth import authenticate, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.html import strip_tags

from apps.auth.cache import clear_previous_session_of_user, cache_session_key_for_request


def login(request):
    """登录模块"""

    if request.method=='GET':
        if request.user.is_authenticated():
            if request.user.is_superuser:
                return HttpResponseRedirect(reverse('admin:index'))
            else:
                return render(request, 'welcome.html')
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
            clear_previous_session_of_user(user)
            auth.login(request=request, user=user)
            cache_session_key_for_request(request)
            if user.is_superuser:
                """管理员账户"""
                return HttpResponseRedirect(reverse('admin:index'))
            else:
                """普通账户"""
                return render(request, 'welcome.html')
        else:
            data = {"msg": '账户或密码错误'}
            return render(request, 'index.html', data)
    else:
        return HttpResponseRedirect(reverse('index'))


def logout_site(request):
    """退出登登录"""

    logout(request)
    return render(request, 'index.html')