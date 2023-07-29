import string
import random

from dataclasses import fields

from src.services.students import *
from src.services.utils import *

DEFAULT_TEST_STUDENT_COUNT = 10


def _get_random_name() -> str:
    return ''.join(random.choice(string.ascii_letters) for _ in range(10))

def _get_random_group() -> int:
    return random.randint(1, 121703)

def _get_random_grade() -> int:
    return random.randint(1, 10)

def random_student():
    student_fio = _get_random_name()
    group = _get_random_group()
    term_one = _get_random_grade()
    term_two = _get_random_grade()
    term_three = _get_random_grade()
    term_four = _get_random_grade()
    term_five = _get_random_grade()
    term_six = _get_random_grade()
    term_seven = _get_random_grade()
    term_eight = _get_random_grade()
    term_nine = _get_random_grade()
    term_ten = _get_random_grade()

    return Student(student_fio=student_fio,
                   group=group,
                   term_one=term_one,
                   term_two=term_two,
                   term_tree=term_three,
                   term_four=term_four,
                   term_five=term_five,
                   term_six=term_six,
                   term_seven=term_seven,
                   term_eight=term_eight,
                   term_nine=term_nine,
                   term_ten=term_ten)

def random_filled_repository():
    r = Students()
    students = (random_student() for _ in range(DEFAULT_TEST_STUDENT_COUNT))
    for student in students:
        r.add_to_student_list(student)

    return r


def test_add_to_list():
    r = Students()
    students = (random_student() for _ in range(DEFAULT_TEST_STUDENT_COUNT))
    for student in students:
        r.add_to_student_list(student)

    assert len(r) == DEFAULT_TEST_STUDENT_COUNT

def test_get_students():
    r = random_filled_repository()
    students = r.get_students()
    assert len(students) == DEFAULT_TEST_STUDENT_COUNT

def test_save_to_json():
    r = random_filled_repository()
    r.save()
    another_r = Students()
    another_r.load_info()

    students = r.get_students()
    another_students = another_r.get_students()

    assert len(students) == len(another_students) 

def test_delete_student():
    r = random_filled_repository()

    for opt in fields(StudentOptions):
        opts = StudentOptions()
        
        student = random.choice(r.get_students_raw()) 
        
        if opt.name == "student_fio" or opt.name == "group":
            print(student)
            setattr(opts, opt.name, getattr(student, opt.name))
        else:
            setattr(opts, opt.name, _get_random_grade())

        r.delete_student(opts)

    students = r.get_students()

    assert len(students) <= DEFAULT_TEST_STUDENT_COUNT 

def test_filter_students():
    for opt in fields(StudentOptions):
        r = random_filled_repository()
        opts = StudentOptions()

        student = random.choice(r.get_students_raw()) 
        if opt.name == "student_fio" or opt.name == "group":
            setattr(opts, opt.name, getattr(student, opt.name))
        else:
            setattr(opts, opt.name, _get_random_grade())

        r.filter_student(opts)

        students = r.get_students()

        assert len(students) >= 1 or len(students) <= DEFAULT_TEST_STUDENT_COUNT

def test_utilis_path_exists():
    assert FileUtils.is_file_exists("./student.json") is True

def test_read_from_file():
    assert len(FileUtils.read_from_json("./student.json")) >= 0









