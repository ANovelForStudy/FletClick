import flet as ft
from functions.clicker import Clicker

import config
from gui.controls.container_without_indents import ContainerWithoutIndents


class StartStopBlock(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Создание объекта кликера
        self.clicker = Clicker()

    def build(self):
        self._start_button = ft.ElevatedButton(
            text="Старт",
            width=120,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.GREEN,
            icon=ft.icons.PLAY_ARROW_ROUNDED,
            # События
            on_click=self.clicker.start_clicker,
        )

        self._stop_button = ft.ElevatedButton(
            text="Стоп",
            width=120,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.RED,
            icon=ft.icons.STOP_ROUNDED,
            # События
            on_click=self.clicker.stop_clicker,
        )

        return ContainerWithoutIndents(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value="УПРАВЛЕНИЕ".upper(),
                        font_family="Inter",
                    ),
                    self._start_button,
                    ft.Divider(height=3),
                    self._stop_button,
                ],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=config.DEFAULT_BLOCK_PADDING,
        )
