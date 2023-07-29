from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField


class AddStudentDialog:
    def __init__(self, controller):
        self._controller = controller

    def build_dialog(self):
        return MDDialog(
            title='New student',
            type='custom',
            content_cls=MDBoxLayout(
                MDTextField(
                    id='student_fio',
                    hint_text="Student's full name",
                    font_size='10',
                    max_text_length=100,
                    helper_text="The field must contain full name",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='group',
                    hint_text="group",
                    font_size='10',
                    max_text_length=10,
                    helper_text="The field must contain the name of the group",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='term_one',
                    hint_text="Term one",
                    font_size='10',
                    max_text_length=2,
                    helper_text="The field must contain a number",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='term_two',
                    hint_text="Term two",
                    font_size='10',
                    max_text_length=2,
                    helper_text="The field must contain a number",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='term_three',
                    hint_text="Term three",
                    font_size='10',
                    max_text_length=2,
                    helper_text="The field must contain a number",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='term_four',
                    hint_text="Term four",
                    font_size='10',
                    max_text_length=2,
                    helper_text="The field must contain a number",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='term_five',
                    hint_text="Term five",
                    font_size='10',
                    max_text_length=2,
                    helper_text="The field must contain a number",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='term_six',
                    hint_text="Term six",
                    font_size='10',
                    max_text_length=2,
                    helper_text="The field must contain a number",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='term_seven',
                    hint_text="Term seven",
                    font_size='10',
                    max_text_length=2,
                    helper_text="The field must contain a number",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='term_eight',
                    hint_text="Term eight",
                    font_size='10',
                    max_text_length=2,
                    helper_text="The field must contain a number",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='term_nine',
                    hint_text="Term nine",
                    font_size='10',
                    max_text_length=2,
                    helper_text="The field must contain a number",
                    helper_text_mode="on_error"
                ),
                MDTextField(
                    id='term_ten',
                    hint_text="Term ten",
                    font_size='10',
                    max_text_length=2,
                    helper_text="The field must contain a number",
                    helper_text_mode="on_error"
                ),
                orientation="vertical",
                spacing="5dp",
                size_hint_y=None,
                height="700dp"
            ),
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    font_style='Button',
                    font_size='17',
                    on_release=lambda event: self.close_dialog()
                ),
                MDRaisedButton(
                    text="Add",
                    font_size='17',
                    md_bg_color='gray',
                    font_style='Button',
                    on_release=lambda event: self.add_student()
                ),
            ],
        )

    def close_dialog(self):
        self._controller.close_dialog()

    def add_student(self):
        self._controller.add_student()
