import flet as ft

import config
from gui.controls.container_without_indents import ContainerWithoutIndents


class SelectingClickLocationBlock(ft.UserControl):
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
            padding=config.DEFAULT_BLOCK_PADDING,
        )
