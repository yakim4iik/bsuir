from kivymd.app import MDApp
from src.services.controller import *
from kivy.core.window import Window

SIZE = {"width": 1170, "height": 1000}
Window.size = (SIZE.get("width"), SIZE.get("height"))
__PROJECT_NAME__ = "Community service"


class App(MDApp):
    """
    The main application class.

    Inherits from kivy.uix.app.App.
    """
    def build(self):
        """
        Builds the graphical application.

        :return: The root view of the graphical application.
        :rtype: kivy.uix.widget.Widget
        """
        self.title = __PROJECT_NAME__
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Pink"
        data = FileUtils.read_from_json("student.json")
        students = Students(State.get_students(data))
        controller = Controller(students)
        return controller.get_root_view()


def main():
    """
    The main entry point for the application.
    """
    app = App()
    app.run()


if __name__ == "__main__":
    main()
