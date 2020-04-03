from apps.users.models import User
from apps.problems.models import CourseTemp

def run():
    course_num_map = {}
    for course in CourseTemp.objects.all():
        course_num_map[course.num] = course

    for user in User.objects.all():
        print('process...', user.account)
        user.course = course_num_map.get(user.choices)
        print('done')

