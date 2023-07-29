from .bar import *
from .table import *
from .dialog_view import *


class View:
    def __init__(self, controller):
        self.dialog = None
        self.controller = controller

        self.bar = Bar(self.controller).build_widget()
        self.table = Table(self.controller).build_widget()

        self.root = MDBoxLayout(self.bar, self.table, orientation='vertical')

    def update_table(self):
        self.root.remove_widget(self.table)
        self.table = Table(self.controller).build_widget()
        self.root.add_widget(self.table)

    def open_add_student_dialog(self):
        self.dialog = AddStudentDialog(self.controller).build_dialog()
        self.dialog.open()

    def open_delete_student_dialog(self):
        self.dialog = DeleteStudentDialog(self.controller).build_dialog()
        self.dialog.open()

    def open_filter_student_dialog(self):
        self.dialog = FilterStudentDialog(self.controller).build_dialog()
        self.dialog.open()


    def close_dialog(self):
        if self.dialog is not None:
            self.dialog.dismiss()
