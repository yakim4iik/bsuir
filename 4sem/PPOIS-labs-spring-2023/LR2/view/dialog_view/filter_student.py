from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField


class FilterStudentDialog:
    def __init__(self, controller) -> None:
        self._controller = controller

    def build_dialog(self) -> MDDialog:
        return MDDialog(
            title="Info",
            type="custom",
            content_cls=MDBoxLayout(
                MDTextField(
                    id='student_fio',
                    hint_text="Student's full name",
                    font_size='10',
                    max_text_length=100,
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='group',
                    hint_text="Group",
                    font_size='10',
                    max_text_length=100,
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='max_community_service',
                    hint_text="Max community service",
                    font_size='10',
                    max_text_length=6,
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='min_community_service',
                    hint_text="Min community service",
                    font_size='10',
                    max_text_length=6,
                    helper_text_mode="on_error"
                ),
                id="form",
                orientation="vertical",
                spacing="4dp",
                size_hint_y=None,
                height="250dp",
            ),
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    theme_text_color="Custom",
                    on_release=lambda event: self._close_dialog(),
                ),
                MDFlatButton(
                    text="Filter",
                    theme_text_color="Custom",
                    on_release=lambda event: self._filter_student(),
                ),
            ],
        )

    def _close_dialog(self) -> None:
        self._controller.close_dialog()

    def _filter_student(self) -> None:
        self._controller.filter_student()
