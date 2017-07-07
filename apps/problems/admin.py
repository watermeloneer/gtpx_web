from django.contrib import admin

# Register your models here.
from apps.problems.models import Problem, Chapter, Course


class ProblemAdmin(admin.ModelAdmin):
    model = Problem



class ChapterAdmin(admin.ModelAdmin):
    model = Chapter



class CourseAdmin(admin.ModelAdmin):
    model = Course


admin.site.register(Course, CourseAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Problem, ProblemAdmin)