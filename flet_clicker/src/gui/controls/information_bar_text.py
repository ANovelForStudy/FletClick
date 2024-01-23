import flet as ft


class InformationBarText(ft.Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.color is None:
            self.color = ft.colors.WHITE

        if self.size is None:
            self.size = 10

        if self.font_family is None:
            self.font_family = "Inter"
