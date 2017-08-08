from django.contrib import admin

# Register your models here.
from apps.exams.models import Exam


class ExamAdmin(admin.ModelAdmin):
    """考试管理后台"""

    model = Exam

    def get_list_display(self, request):
        return [f.name for f in self.model._meta.fields]

admin.site.register(Exam, ExamAdmin)
