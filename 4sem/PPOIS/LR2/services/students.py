import dataclasses
from typing import Optional
from .utils import FileUtils


class Students:
    def __init__(self, collection) -> None:
        self.__students = collection

    def to_dict(self):
        data = dict()
        data["students"] = [student.to_dict() for student in self.__students]
        return data

    def add_to_student_list(self, student):
        if student not in self.__students:
            self.__students.append(student)
            self.save()

    def get_students(self):
        students_data = [student.get_student_info() for student in self.__students]
        return students_data

    def load_info(self):
        data = FileUtils.read_from_json("student.json")
        self.__students = State.get_students(data)

    def save(self):
        data = self.to_dict()
        FileUtils.save_in_json(data, "student.json")

    def delete_student(self, opts):
        if opts.student_fio:
            self.delete_by_student_fio(opts.student_fio)
        if opts.group:
            self.delete_by_group(opts.group)
        if opts.min_community_service and opts.max_community_service and opts.student_fio:
            self.delete_by_service_and_fio(opts.min_community_service, opts.max_community_service, opts.student_fio)
        if opts.min_community_service and opts.max_community_service and opts.group:
            self.delete_by_service_and_group(opts.min_community_service, opts.max_community_service, opts.group)
        self.save()

    def delete_by_student_fio(self, fio):
        students = []
        for student in self.__students:
            if fio in student.student_fio:
                students.append(student)
        for student in students:
            self.__students.remove(student)

    def delete_by_group(self, group):
        students = []
        for student in self.__students:
            if group in student.group:
                students.append(student)
        for student in students:
            self.__students.remove(student)

    def delete_by_service_and_fio(self, min_community_service=None, max_community_service=None, student_fio=None):
        students = []
        if min_community_service and max_community_service and student_fio:
            for student in self.__students:
                total = 0
                for properties in vars(student):
                    if type(properties) == int:
                        total += properties
                if int(max_community_service) >= total >= int(min_community_service) \
                        and student_fio in student.student_fio:
                    students.append(student)
        elif min_community_service and student_fio:
            for student in self.__students:
                total = 0
                for properties in student:
                    if type(properties) == int:
                        total += properties
                if int(min_community_service) <= total and student_fio in student.student_fio:
                    students.append(student)
        elif max_community_service and student_fio:
            for student in self.__students:
                total = 0
                for properties in student:
                    if type(properties) == int:
                        total += properties
                if int(max_community_service) >= total and student_fio in student.student_fio:
                    students.append(student)
        for student in students:
            self.__students.remove(student)

    def delete_by_service_and_group(self, min_community_service=None, max_community_service=None, group=None):
        students = []
        if min_community_service and max_community_service and group:
            for student in self.__students:
                total = 0
                for properties in student:
                    if type(properties) == int:
                        total += properties
                if int(max_community_service) >= total >= int(min_community_service) and group in student.group:
                    students.append(student)
        elif min_community_service and group:
            for student in self.__students:
                total = 0
                for properties in student:
                    if type(properties) == int:
                        total += properties
                if int(min_community_service) <= total and group in student.group:
                    students.append(student)
        elif max_community_service and group:
            for student in self.__students:
                total = 0
                for properties in student:
                    if type(properties) == int:
                        total += properties
                if int(max_community_service) >= total and group in student.group:
                    students.append(student)
        for student in students:
            self.__students.remove(student)

    def filter_student(self, opts):
        self.load_info()
        if opts.student_fio:
            self.filter_by_student_fio(opts.student_fio)
        if opts.group:
            self.filter_group(opts.group)
        if opts.min_community_service and opts.max_community_service and opts.student_fio:
            self.filter_by_service_and_fio(opts.min_community_service, opts.max_community_service, opts.student_fio)
        if opts.min_community_service and opts.max_community_service and opts.group:
            self.filter_by_service_and_group(opts.min_community_service, opts.max_community_service, opts.group)

    def filter_by_student_fio(self, fio):
        students = []
        for student in self.__students:
            if fio not in student.student_fio:
                students.append(student)
        for student in students:
            self.__students.remove(student)

    def filter_group(self, group):
        students = []
        for student in self.__students:
            if group not in student.group:
                students.append(student)
        for student in students:
            self.__students.remove(student)

    def filter_by_service_and_fio(self, min_community_service=None, max_community_service=None, student_fio=None):
        students = []
        if min_community_service and max_community_service and student_fio:
            for student in self.__students:
                total = 0
                for properties in student:
                    if type(properties) == int:
                        total += properties
                if int(max_community_service) < total or total < int(min_community_service) \
                        or student_fio not in student.student_fio:
                    students.append(student)
        elif min_community_service and student_fio:
            for student in self.__students:
                total = 0
                for properties in student:
                    if type(properties) == int:
                        total += properties
                if int(min_community_service) > total or student_fio not in student.student_fio:
                    students.append(student)
        else:
            for student in self.__students:
                total = 0
                for properties in student:
                    if type(properties) == int:
                        total += properties
                if int(max_community_service) < total or student_fio not in student.student_fio:
                    students.append(student)
        for student in students:
            self.__students.remove(student)

    def filter_by_service_and_group(self, min_community_service=None, max_community_service=None, group=None):
        students = []
        if min_community_service and max_community_service and group:
            for student in self.__students:
                total = 0
                for properties in student:
                    if type(properties) == int:
                        total += properties
                if int(max_community_service) < total or total < int(min_community_service) \
                        or group not in student.group:
                    students.append(student)
        elif min_community_service and group:
            for student in self.__students:
                total = 0
                for properties in student:
                    if type(properties) == int:
                        total += properties
                if int(min_community_service) > total or group not in student.group:
                    students.append(student)
        else:
            for student in self.__students:
                total = 0
                for properties in student:
                    if type(properties) == int:
                        total += properties
                if int(max_community_service) < total and group not in student.group:
                    students.append(student)
        for student in students:
            self.__students.remove(student)


class Student:
    def __init__(self,
                 student_fio=None,
                 group=None,
                 term_one=None,
                 term_two=None,
                 term_tree=None,
                 term_four=None,
                 term_five=None,
                 term_six=None,
                 term_seven=None,
                 term_eight=None,
                 term_nine=None,
                 term_ten=None):
        self.student_fio = student_fio
        self.group = group
        self.term_one = term_one
        self.term_two = term_two
        self.term_three = term_tree
        self.term_four = term_four
        self.term_five = term_five
        self.term_six = term_six
        self.term_seven = term_seven
        self.term_eight = term_eight
        self.term_nine = term_nine
        self.term_ten = term_ten

    def to_dict(self):
        data = dict()
        data['student_fio'] = self.student_fio
        data['group'] = self.group
        data['term_one'] = self.term_one
        data['term_two'] = self.term_two
        data['term_three'] = self.term_three
        data['term_four'] = self.term_four
        data['term_five'] = self.term_five
        data['term_six'] = self.term_six
        data['term_seven'] = self.term_seven
        data['term_eight'] = self.term_eight
        data['term_nine'] = self.term_nine
        data['term_ten'] = self.term_ten
        return data

    def get_student_info(self):
        student_info = self.to_dict()
        return tuple(student_info.values())


@dataclasses.dataclass
class StudentOptions:
    student_fio: Optional[str]
    group: Optional[str]
    min_community_service: Optional[int]
    max_community_service: Optional[int]


class State:
    @staticmethod
    def get_students(data: dict):
        students = []
        for student in data["students"]:
            student_data = Student(*student.values())
            students.append(student_data)
        return students
