import dataclasses
from typing import Optional
from .utils import FileUtils


class Students:
    """
    Provides a convenient API for working with students
    
    :param collection: Initial list of students
    :type collection: list
    """
    def __init__(self, collection=None) -> None:
        """
        Initializes the Students object with a collection of students.

        :param collection: the initial list of students, defaults to None
        :type collection: list, optional
        """
        self.__students = collection if collection is not None else []

    def to_dict(self):
        """
        Returns the students as a dictionary.

        :return: the students as a dictionary
        :rtype: dict
        """
        data = dict()
        data["students"] = [student.to_dict() for student in self.__students]
        return data

    def __len__(self) -> int:
        """
        Returns the number of students in the collection.

        :return: the number of students
        :rtype: int
        """
        return len(self.__students)

    def add_to_student_list(self, student):
        """
        Adds a student to the collection.

        :param student: the student to be added
        :type student: src.models.student.Student
        """
        if student not in self.__students:
            self.__students.append(student)
            self.save()

    def get_students_raw(self):
        """
        Returns theraw list of students in the collection.

        :return: the raw list of students
        :rtype: list
        """
        return self.__students

    def get_students(self):
        """
        Returns a list of dictionaries, each containing information about a student.

        :return: a list of dictionaries containing student information
        :rtype: list
        """
        students_data = [student.get_student_info() for student in self.__students]
        return students_data

    def load_info(self):
        """
        Loads student information from a JSON file and sets it as the collection of students.
        """
        data = FileUtils.read_from_json("../student.json")
        self.__students = State.get_students(data)

    def save(self):
        """
        Saves the collection of students to a JSON file.
        """
        data = self.to_dict()
        FileUtils.save_in_json(data, "../student.json")

    def delete_student(self, opts):
        """
        Deletes a student from the collection based on the specified options.

        :param opts: the options for deleting the student
        :type opts: argparse.Namespace
        """
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
        """
        Deletes a student from the collection by their name.

        :param fio: the name of the student to be deleted
        :type fio: str
        """
        students = []
        for student in self.__students:
            if fio == student.student_fio:
                students.append(student)
        for student in students:
            self.__students.remove(student)

    def delete_by_group(self, group):
        """
        Deletes students from the collection by their group.

        :param group: the group of the students to be deleted
        :type group: str
        """
        students = []
        for student in self.__students:
            if group == student.group:
                students.append(student)
        for student in students:
            self.__students.remove(student)

    def delete_by_service_and_fio(self, min_community_service=None, max_community_service=None, student_fio=None):
        """
        Deletes students from the collection by their name and their community service hours.

        :param min_community_service: the minimum number of community service hours
        :type min_community_service: int, optional
        :param max_community_service: the maximum number of community service hours
        :type max_community_service: int, optional
        :param student_fio: the name of the student
        :type student_fio: str, optional
        """
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
        """
        Deletes students from the collection by their group and their community service hours.

        :param min_community_service: the minimum number of community service hours
        :type min_community_service: int, optional
        :param max_community_service: the maximum number of community service hours
        :type max_community_service: int, optional
        :param group: group number
        :type group: str, optional
        """
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
        """
        Filters the list of Student objects based on the specified options.

        :param opts: the options for filtering the list of Student objects
        :type opts: StudentOptions
        """
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
        """
        Filters the list of Student objects by the specified name.

        :param fio: the name to filter by
        :type fio: str
        """
        students = []
        for student in self.__students:
            if fio != student.student_fio:
                students.append(student)
        for student in students:
            self.__students.remove(student)

    def filter_group(self, group):
        """
        Filters students from the collection by their group.

        :param group: the group of the students to be deleted
        :type group: str
        """
        students = []
        for student in self.__students:
            if group != student.group:
                students.append(student)
        for student in students:
            self.__students.remove(student)

    def filter_by_service_and_fio(self, min_community_service=None, max_community_service=None, student_fio=None):
        """
        Filters students from the collection by their name and their community service hours.

        :param min_community_service: the minimum number of community service hours
        :type min_community_service: int, optional
        :param max_community_service: the maximum number of community service hours
        :type max_community_service: int, optional
        :param student_fio: the name of the student
        :type student_fio: str, optional
        """
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
        """
        Filters students from the collection by their group and their community service hours.

        :param min_community_service: the minimum number of community service hours
        :type min_community_service: int, optional
        :param max_community_service: the maximum number of community service hours
        :type max_community_service: int, optional
        :param group: group number
        :type group: str, optional
        """
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
        """
        Initializes a new instance of the Student class.
        """
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
        """
        Converts a Student object to a dictionary.

        :return: A dictionary representing the Student object.
        :rtype: dict
        """
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
    """
    Represents options for filtering students.
    """
    student_fio: Optional[str] = None
    group: Optional[str] = None
    min_community_service: Optional[int] = None
    max_community_service: Optional[int] = None


class State:
    @staticmethod
    def get_students(data: dict):
        """
        Extracts a list of Student objects from a dictionary of student data.

        :param data: A dictionary containing student data.
        :type data: dict
        :return: A list of Student objects.
        :rtype: list[Student]
        """
        students = []
        for student in data["students"]:
            student_data = Student(*student.values())
            students.append(student_data)
        return students
