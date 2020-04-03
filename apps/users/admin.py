# -*- conding:utf-8 -*-

from django.contrib import admin
from apps.users.models import User



class UserAdmin(admin.ModelAdmin):
    search_fields = ('name', 'account')
    list_display = ('id', 'account', 'name', 'password', 'create_time', 'course')
    date_hierarchy = 'create_time'
    exclude = ('create_time',)
    model = User


admin.site.register(User, UserAdmin)
admin.AdminSite.site_header ='国通培训管理系统'
admin.AdminSite.site_title = '国通培训管理系统'