from ..view import *
from .students import *


class Controller:
    """A class designed to control the state of a graphical application. 
    Also provides a convenient interface for interacting with the data storage layer.
    Mainly interacts with :class:`src.view.view` class.

    :param repository: Initial students object 
    :type repository: class:`src.services.Students`
    """
    def __init__(self, repository: Students):
        self.repository = repository
        self.view = View(self)

    def get_root_view(self):
        """
        Returns the root view of the graphical application.

        :return: The root view of the graphical application.
        :rtype: kivy.uix.widget.Widget
        """
        return self.view.root

    def close_dialog(self):
        """
        Closes the current dialog.
        """
        self.view.close_dialog()

    def add_student(self):
        """
        Adds a new student to the data storage layer.
        """
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
        """
        Deletes a student from the data storage layer.
        """
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
        """
        Filters the list of students in the data storage layer.
        """
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
        """
        Returns a list of all students in the data storage layer.

        :return: A list of all students in the data storage layer.
        :rtype: list[Student]
        """
        return self.repository.get_students()

    def open_add_dialog(self):
        """
        Opens the dialog for adding a new studentto the graphical application.
        """
        self.view.open_add_student_dialog()

    def open_delete_dialog(self):
        """
        Opens the dialog for deleting a student from the graphical application.
        """
        self.view.open_delete_student_dialog()

    def open_filter_dialog(self):
        """
        Opens the dialog for filtering the list of students in the graphical application.
        """
        self.view.open_filter_student_dialog()
