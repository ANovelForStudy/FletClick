import flet as ft

import config
from gui.controls.container_without_indents import ContainerWithoutIndents


class SelectingTypeOfClicksBlock(ft.UserControl):
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
            padding=config.DEFAULT_BLOCK_PADDING,
        )
