from django.contrib import admin

# Register your models here.
from apps.problems.models import Problem, Chapter, Course, ProbelmTemp, CategoryTemp, CourseTemp


class ProblemAdmin(admin.ModelAdmin):
    model = Problem



class ChapterAdmin(admin.ModelAdmin):
    model = Chapter



class CourseAdmin(admin.ModelAdmin):
    model = Course


class CourseTempAdmin(admin.ModelAdmin):
    model = CourseTemp


class CategoryTempAdmin(admin.ModelAdmin):
    model = CategoryTemp


class ProbelmTempAdmin(admin.ModelAdmin):
    model = ProbelmTemp


# admin.site.register(Course, CourseAdmin)
# admin.site.register(Chapter, ChapterAdmin)
# admin.site.register(Problem, ProblemAdmin)
admin.site.register(CourseTemp, CourseTempAdmin)
admin.site.register(CategoryTemp, CategoryTempAdmin)
admin.site.register(ProbelmTemp, ProbelmTempAdmin)