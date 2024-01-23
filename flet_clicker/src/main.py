import sys
from typing import Optional

import flet as ft
from icecream import ic

import config
from gui.side_bar import Sidebar
from gui.status_bar import StatusBar
from gui.top_bar import TopBar


class App:
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page

        self.set_window_size()
        self.set_page_padding()

        # Set color scheme and light mode
        self.set_light_mode()
        self.set_color_scheme(color_scheme_seed="yellow")

        self.page.add(
            ft.Container(
                ft.Row(
                    controls=[
                        ft.Column(controls=[], expand=True),
                        Sidebar(),
                    ]
                ),
                expand=True,
            )
        )

        self.page.update()

    def set_window_size(self):
        self.page.window_height = config.WINDOW_HEIGHT
        self.page.window_width = config.WINDOW_WIDTH
        self.page.window_resizable = False
        self.page.window_maximizable = False

    def set_page_padding(self):
        self.page.padding = ft.Padding(
            left=config.PAGE_PADDING_LEFT,
            right=config.PAGE_PADDING_RIGHT,
            top=config.PAGE_PADDING_TOP,
            bottom=config.PAGE_PADDING_BOTTOM,
        )

    def set_light_mode(self) -> None:
        self.page.theme_mode = ft.ThemeMode.LIGHT

    def set_color_scheme(self, color_scheme_seed: Optional[str] = None) -> None:
        if color_scheme_seed is not None:
            self.page.theme = ft.Theme(color_scheme_seed=color_scheme_seed)


if __name__ == "__main__":
    config.add_main_directory_to_path()
    ic(sys.path)
    ft.app(target=App, view=ft.AppView.FLET_APP)
