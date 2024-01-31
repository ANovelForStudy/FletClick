import sys
from typing import Optional

import flet as ft
from icecream import ic

import config
from gui.blocks.side_bar import Sidebar
from gui.blocks.status_bar import StatusBar
from gui.blocks.top_bar import TopBar
from gui.pages.first.first_page_main_content import MainContentFirstPage
from gui.pages.second.second_page_main_content import MainContentSecondPage


class App:
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page

        self.set_window_size()
        self.set_page_padding()

        # Set color scheme and light mode
        self.set_light_mode()
        self.set_color_scheme(color_scheme_seed="blue")

        # Построение интерфейса приложения
        self.build_ui()

    #
    # ПОСТРОЕНИЕ ИНТЕРФЕЙСА
    #

    def build_ui(self):
        self.page.add(
            # Внешний контейнер страницы
            ft.Container(
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                TopBar(),
                                ft.Tabs(
                                    # Выбор индекса вкладки по умолчанию
                                    selected_index=config.Pages.main_clicker_settings_page,
                                    animation_duration=300,
                                    tabs=[
                                        ft.Tab(
                                            icon=ft.icons.POWER_SETTINGS_NEW,
                                            text="Кликер",
                                            content=MainContentFirstPage(),
                                        ),
                                        ft.Tab(
                                            icon=ft.icons.ADS_CLICK,
                                            text="Место/Тип",
                                            content=MainContentSecondPage(),
                                        ),
                                        ft.Tab(
                                            icon=ft.icons.SETTINGS,
                                            text="Настройки",
                                            # content=MainContent(),
                                        ),
                                    ],
                                    expand=True,
                                ),
                                StatusBar(),
                            ],
                            expand=True,
                            spacing=0,
                        ),
                        Sidebar(),
                    ],
                    spacing=0,
                ),
                expand=True,
                padding=0,
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

    def set_fonts(self) -> None:
        self.page.fonts = {
            "Inter": "/fonts/Inter.ttf",
        }


if __name__ == "__main__":
    config.add_main_directory_to_path()

    ic(sys.path)

    ft.app(
        target=App,
        view=ft.AppView.FLET_APP,
        assets_dir="assets",
    )
