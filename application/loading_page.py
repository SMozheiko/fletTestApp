from flet import Page, ProgressRing, MainAxisAlignment, Row, AlertDialog, Column, Padding
from flet_core import Text, FontWeight, CrossAxisAlignment


class LoadingPage:

    def __init__(self, page: Page):
        self.page = page
        self.progress = Row(
            controls=[ProgressRing(width=64, height=64, stroke_width=10)],
            alignment=MainAxisAlignment.CENTER
        )
        self.tip = Text('Идет загрузка', weight=FontWeight.BOLD, width=200)
        self.alert = AlertDialog(
            content=Column(
                controls=[self.progress, self.tip],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                height=self.progress.controls[0].height + 50,
            ),
            content_padding=Padding(30, 30, 30, 30)
        )

    def stop(self):
        self.alert.open = False
        self.page.update()

    def render(self):
        self.page.dialog = self.alert
        self.alert.open = True
        self.page.update()
