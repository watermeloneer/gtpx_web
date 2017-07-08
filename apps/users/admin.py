from django.contrib import admin

# Register your models here.
from apps.users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'name', 'choices', 'password', 'create_time', )
    date_hierarchy = 'create_time'
    exclude = ('create_time',)
    model = User


admin.site.register(User, UserAdmin)