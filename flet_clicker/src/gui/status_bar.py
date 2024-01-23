import flet as ft

# from controls.bar import LabelContainer
import config
from gui.controls.information_bar_text import InformationBarText
from gui.controls.label_container import LabelContainer


class StatusBar(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._label_program_status = "Статус: ЗАГЛУШКА"
        # self._label_click_count = "Количество нажатий: ЗАГЛУШКА "

        # self._label_information = f"{self._label_program_status} | {self._label_click_count}".upper()
        self._label_information = f"{self._label_program_status}".upper()

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
            bgcolor=config.STATUSBAR_COLOR,
        )
