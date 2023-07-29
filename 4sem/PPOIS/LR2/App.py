from kivymd.app import MDApp
from services.controller import *
from kivy.core.window import Window

SIZE = {"width": 1170, "height": 1000}
Window.size = (SIZE.get("width"), SIZE.get("height"))
__PROJECT_NAME__ = "Community service"


class App(MDApp):
    def build(self):
        self.title = __PROJECT_NAME__
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Pink"
        data = FileUtils.read_from_json("student.json")
        students = Students(State.get_students(data))
        controller = Controller(students)
        return controller.get_root_view()


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()
