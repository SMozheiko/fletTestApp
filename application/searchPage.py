from time import sleep

from flet import Page, OutlinedButton, Column, Row, TextField, Control, Text, MainAxisAlignment, CrossAxisAlignment,\
    InputBorder, FontWeight, ListView
from flet_core import ControlEvent

from application.loading_page import LoadingPage


class SearchPage:

    _data = [
        "first",
        "firstValue",
        "second",
        "secondValue"
    ]

    def __init__(self, page: Page):
        self.page = page
        self.input = TextField(label=None, border=InputBorder.UNDERLINE, on_change=self.on_change)
        self.suggestions = ListView(width=self.input.width)
        self.suggestions.visible = False
        self.input_column = Column(
            controls=[
                self.input,
                self.suggestions
            ]
        )
        self.label = Text(value="Введите номер: ", size=18, weight=FontWeight.BOLD)
        self.confirm_button = OutlinedButton("Продолжить", on_click=self.on_click, disabled=True)

    def on_change(self, event: ControlEvent):
        self.confirm_button.disabled = not bool(self.input.value)
        self.suggestions.controls.clear()
        if self.input.value:
            for i in self._data:
                if i.startswith(self.input.value):
                    self.suggestions.controls.append(
                        Text(i)
                    )
            if self.suggestions.controls:
                self.suggestions.visible = True
        self.page.update()

    def on_click(self, event: ControlEvent):
        animation = LoadingPage(self.page)
        animation.render()
        counter = 10
        dots = [3, 2, 1]
        dot = ' .'
        while counter:
            count = dots.pop()
            animation.tip.value = 'Идет загрузка' + dot * count
            dots.insert(0, count)
            self.page.update()
            sleep(1)
            counter -= 1
        animation.stop()

    def _create_view(self) -> Control:
        self.page.horizontal_alignment = CrossAxisAlignment.CENTER
        self.page.vertical_alignment = MainAxisAlignment.CENTER
        input_row = Row(
            controls=[self.label, self.input_column],
            alignment=MainAxisAlignment.SPACE_EVENLY,
            width=self.page.width * 0.6
        )
        control_row = Row(
            controls=[self.confirm_button],
            alignment=MainAxisAlignment.END,
            width=self.page.width * 0.6
        )
        column = Column(
            controls=[input_row, control_row],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
        return column

    def render(self):
        self.page.clean()
        self.page.add(self._create_view())
        self.page.update()
