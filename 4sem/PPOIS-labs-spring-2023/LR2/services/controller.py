from view.view import *
from .students import *


class Controller:
    def __init__(self, repository: Students):
        self.repository = repository
        self.view = View(self)

    def get_root_view(self):
        return self.view.root

    def close_dialog(self):
        self.view.close_dialog()

    def add_student(self):
        data = self.view.dialog.content_cls.ids

        student = Student(data.student_fio.text,
                          data.group.text,
                          data.term_one.text,
                          data.term_two.text,
                          data.term_three.text,
                          data.term_four.text,
                          data.term_five.text,
                          data.term_six.text,
                          data.term_seven.text,
                          data.term_eight.text,
                          data.term_nine.text,
                          data.term_ten.text)

        self.repository.add_to_student_list(student)

        self.view.close_dialog()
        self.view.update_table()

    def delete_student(self):
        data = self.view.dialog.content_cls.ids
        opts = StudentOptions(student_fio=data.student_fio.text,
                              group=data.group.text,
                              min_community_service=data.min_community_service.text,
                              max_community_service=data.max_community_service.text,
                              )

        self.repository.delete_student(opts)

        self.view.close_dialog()
        self.view.update_table()

    def filter_student(self):
        data = self.view.dialog.content_cls.ids
        opts = StudentOptions(student_fio=data.student_fio.text,
                              group=data.group.text,
                              min_community_service=data.min_community_service.text,
                              max_community_service=data.max_community_service.text,
                              )
        self.repository.filter_student(opts)

        self.view.close_dialog()
        self.view.update_table()
        self.repository.load_info()

    def get_student(self):
        return self.repository.get_students()

    def open_add_dialog(self):
        self.view.open_add_student_dialog()

    def open_delete_dialog(self):
        self.view.open_delete_student_dialog()

    def open_filter_dialog(self):
        self.view.open_filter_student_dialog()
