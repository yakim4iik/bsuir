from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton


class Bar:
    """
    Bar view widget

    :param controller: view controller
    :type controller: class:`src.services.controller.Controller` 
    """
    def __init__(self, controller) -> None:
        self._controller = controller

    def build_widget(self) -> MDBoxLayout:
        """
        Builds the widget for the Bar view.

        :return: the built widget
        :rtype: kivymd.uix.boxlayout.MDBoxLayout
        """
        return MDBoxLayout(
            MDRaisedButton(
                text="Добавить",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self.add_student()
            ),
            MDRaisedButton(
                text="Удалить",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self.delete_student()
            ),
            MDRaisedButton(
                text="Фильтр",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self.filter_student()
            ),

            id="bar",
            size=(200, 100),
            size_hint=(1, None),
            spacing=10,
            padding=10
        )

    def add_student(self) -> None:
        """
        Calls the open_add_dialog function of the controller class, in which
        opens a dialog box for adding a new student.
        """
        self._controller.open_add_dialog()

    def delete_student(self) -> None:
        """
        Calls the open_delete_dialog function of the controller class, in which
        opens a dialog box for deleting a student.
        """
        self._controller.open_delete_dialog()

    def filter_student(self) -> None:
        """
        Calls the open_filter_dialog function of the controller class, in which
        opens a dialog box for filtering students.
        """
        self._controller.open_filter_dialog()




