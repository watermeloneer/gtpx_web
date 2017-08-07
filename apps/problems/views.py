# _*_ coding:utf-8 _*_
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def problems_view(request):
    """做题页面"""
    data = {'level': int(request.GET.get('level', 0))}
    return render(request, 'welcome.html', context=data)


