import flet as ft

import config


class MainContent(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            GuiRandomizingTimeBetweenTaps(),
                        ],
                    ),
                    ft.Row(
                        controls=[],
                    ),
                    ft.Row(
                        controls=[],
                    ),
                ]
            ),
            margin=0,
            padding=0,
            expand=True,
            bgcolor="yellow",
        )


class GuiRandomizingTimeBetweenTaps(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        bgcolor="blue",
                    ),
                ]
            ),
            margin=0,
            padding=0,
            bgcolor="red",
        )
