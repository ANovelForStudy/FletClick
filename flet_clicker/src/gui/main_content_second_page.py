import flet as ft

import config
from gui.controls.container_without_indents import ContainerWithoutIndents


class MainContentSecond(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        return ContainerWithoutIndents(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            GuiClickLocation(),
                            GuiTypeOfClicks(),
                        ],
                        spacing=3,
                    ),
                    ft.Row(
                        controls=[],
                        spacing=3,
                    ),
                ],
                spacing=0,
            ),
        )


class GuiClickLocation(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        self._cursor_click = ft.CupertinoRadio(
            value=1,
        )

        self._coordinate_click = ft.CupertinoRadio(
            value=2,
        )

        return ContainerWithoutIndents(
            # debug=True,
            content=ft.Column(
                controls=[
                    ft.Text(
                        value="МЕСТО НАЖАТИЯ".upper(),
                        font_family="Inter",
                    ),
                    ft.RadioGroup(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        self._cursor_click,
                                        ft.Text("По курсору"),
                                    ],
                                    spacing=3,
                                ),
                                ft.Row(
                                    controls=[
                                        self._coordinate_click,
                                        ft.Text("По заданным координатам"),
                                        ft.Text(
                                            "(x=116, y=673)",
                                            selectable=True,
                                        ),
                                    ],
                                    spacing=3,
                                ),
                            ],
                            spacing=3,
                        ),
                    ),
                ],
                spacing=0,
            ),
            padding=5,
        )


class GuiTypeOfClicks(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        self._radio_single_click = ft.CupertinoRadio(
            value=1,
        )
        self._radio_double_click = ft.CupertinoRadio(
            value=2,
        )
        return ContainerWithoutIndents(
            # debug=True,
            content=ft.Column(
                controls=[
                    ft.Text(
                        value="ТИП НАЖАТИЙ".upper(),
                        font_family="Inter",
                    ),
                    ft.RadioGroup(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        self._radio_single_click,
                                        ft.Text("Одинарный"),
                                    ],
                                    spacing=3,
                                ),
                                ft.Row(
                                    controls=[
                                        self._radio_double_click,
                                        ft.Text("Двойной"),
                                    ],
                                    spacing=3,
                                ),
                            ],
                            spacing=3,
                        ),
                    ),
                ],
                spacing=0,
            ),
            padding=5,
        )