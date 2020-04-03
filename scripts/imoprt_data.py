import json

from apps.problems.models import CourseTemp, ChapterTemp, ProbelmTemp
from study.settings import BASE_DIR
import os

def load_json_file(fpath):
    print(fpath)
    with open(fpath, 'r') as f:
        data = json.loads(f.read())
        return data


def import_courses(courses):
    """导入课程
    """
    for course_info in courses:
        _, created = CourseTemp.objects.get_or_create(num=course_info['num'], name=course_info['name'])
        print(created)


def import_chapters(chapters, course, level=0):
    """导入章节目录
    """
    for chapter in chapters:
        _, created = ChapterTemp.objects.get_or_create(num=chapter['num'], name=chapter['name'], course=course, level=level)
        print(created)


def import_questions(questions, course, chapter, level=0):

    CATEGORY_MAP = {
        '单选题': 0,
        '判断题': 1,
        '多选题': 2,
        '图片题': 3,
        '数字类选择题': 4,
    }

    problems = []
    for q in questions:
        print(q)
        params = {
            "course": course,
            "chapter": chapter,
            "level": level,
            "num": q.get('num'),
            "images": q.get('images'),
            "title": q['title'],
            "choices": q['choices'],
            "answers": q['answers'],
            "category": CATEGORY_MAP[q['category']],
        }

        problem = ProbelmTemp(**params)
        problems.append(problem)

    ProbelmTemp.objects.bulk_create(problems, batch_size=100)


def run():
    dir_names = [
        '202001',
        '202002',
        '202003',
        '202004',
    ]
    for name in dir_names:
        _run(name)

def _run(dir_name):
    print('start...')
    BASE_DATA_DIR = os.path.join(BASE_DIR, 'scripts/html/data/')
    DATA_DIR = os.path.join(BASE_DATA_DIR, dir_name)
    course_file = os.path.join(DATA_DIR, 'courses.json')
    chapters_file = os.path.join(DATA_DIR, 'chapters.json')
    questions_file = os.path.join(DATA_DIR, 'questions.json')

   
    courses = load_json_file(course_file)
    import_courses(courses)
    course = courses[0]['num']
    
    chapters = load_json_file(chapters_file)
    import_chapters(chapters, course=course, level=0)
    chapter = chapters[0]['num']

    questions = load_json_file(questions_file)
    import_questions(questions, course=course, chapter=chapter, level=0)
    print('done.')

if __name__ == "__main__":
    run()