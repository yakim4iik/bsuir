from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout


class Table:
    def __init__(self, controller) -> None:
        self._controller = controller

    def build_widget(self) -> MDBoxLayout:
        return MDBoxLayout(
            MDDataTable(
                padding=10,
                elevation=0,
                use_pagination=True,
                pagination_menu_height=330,
                check=True,
                column_data=[
                    ("Student's full name", dp(50)),
                    ("Group", dp(20)),
                    ("1 term", dp(15)),
                    ("2 term", dp(15)),
                    ("3 term", dp(15)),
                    ("4 term", dp(15)),
                    ("5 term", dp(15)),
                    ("6 term", dp(15)),
                    ("7 term", dp(15)),
                    ("8 term", dp(15)),
                    ("9 term", dp(15)),
                    ("10 term", dp(15))
                ],
                row_data=self._controller.get_student()
            ),
            id="table",
        )
