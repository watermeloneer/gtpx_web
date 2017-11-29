from django.contrib import admin

# Register your models here.
from apps.problems.models import ProbelmTemp, ChapterTemp, CourseTemp


#  Problem, Chapter, Course,

# class ProblemAdmin(admin.ModelAdmin):
#     model = Problem
#
#
#
# class ChapterAdmin(admin.ModelAdmin):
#     model = Chapter
#
#
#
# class CourseAdmin(admin.ModelAdmin):
#     model = Course


class CourseTempAdmin(admin.ModelAdmin):
    model = CourseTemp

    # def get_readonly_fields(self, request, obj=None):
    #     return [f.name for f in self.model._meta.fields]


class CategoryTempAdmin(admin.ModelAdmin):
    model = ChapterTemp

    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields]


class ProbelmTempAdmin(admin.ModelAdmin):
    model = ProbelmTemp

    search_fields = ('title',)

    def get_list_display(self, request):
        return [f.name for f in self.model._meta.fields]

    # def get_readonly_fields(self, request, obj=None):
    #     return [f.name for f in self.model._meta.fields]


# admin.site.register(Course, CourseAdmin)
# admin.site.register(Chapter, ChapterAdmin)
# admin.site.register(Problem, ProblemAdmin)
admin.site.register(CourseTemp, CourseTempAdmin)
admin.site.register(ChapterTemp, CategoryTempAdmin)
admin.site.register(ProbelmTemp, ProbelmTempAdmin)
