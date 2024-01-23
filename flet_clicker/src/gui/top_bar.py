import flet as ft

import config
from gui.controls.information_bar_text import InformationBarText
from gui.controls.label_container import LabelContainer


class TopBar(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._label_information = f"Версия {config.VERSION} | Разработчик: {config.DEVELOPER}".upper()

    def build(self):
        return LabelContainer(
            content=ft.Row(
                controls=[
                    InformationBarText(
                        value=self._label_information,
                    ),
                ],
                expand=True,
            ),
            bgcolor=config.TOPBAR_COLOR,
        )
