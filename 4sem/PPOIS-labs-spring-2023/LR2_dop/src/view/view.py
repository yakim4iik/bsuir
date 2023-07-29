from .bar import *
from .table import *
from .dialog_view import *


class View:
    """
    Main view with table and bar widgets

    :param controller: view controller
    :type controller: class:`src.services.controller.Controller` 
    """
    def __init__(self, controller):
        """
        Initializes the View object with a controller, and creates the bar and table widgets.

        :param controller: the controller for the view
        :type controller: src.services.controller.Controller
        """
        self.dialog = None
        self.controller = controller

        self.bar = Bar(self.controller).build_widget()
        self.table = Table(self.controller).build_widget()

        self.root = MDBoxLayout(self.bar, self.table, orientation='vertical')

    def update_table(self):
        """
        Removes the current table widget and replaces it with a new table widget, updated with the latest data.
        """
        self.root.remove_widget(self.table)
        self.table = Table(self.controller).build_widget()
        self.root.add_widget(self.table)

    def open_add_student_dialog(self):
        """
        Opens the dialog box for adding a new student.
        """
        self.dialog = AddStudentDialog(self.controller).build_dialog()
        self.dialog.open()

    def open_delete_student_dialog(self):
        """
        Opens the dialog box for deleting a student.
        """
        self.dialog = DeleteStudentDialog(self.controller).build_dialog()
        self.dialog.open()

    def open_filter_student_dialog(self):
        """
        Opens the dialog box for filtering students.
        """
        self.dialog = FilterStudentDialog(self.controller).build_dialog()
        self.dialog.open()


    def close_dialog(self):
        """
        Closes the dialog box if it is open.
        """
        if self.dialog is not None:
            self.dialog.dismiss()
