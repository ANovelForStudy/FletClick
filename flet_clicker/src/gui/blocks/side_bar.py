import flet as ft
from functions.sidebar_functions import upload_configuration_file

import config
from gui.controls.container_without_indents import ContainerWithoutIndents


class Sidebar(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        return ContainerWithoutIndents(
            ft.Column(
                controls=[
                    self.SidebarIcon(
                        ft.icons.UPLOAD_FILE,
                        tooltip="Загрузить файл настроек кликера",
                    ),
                    self.SidebarIcon(ft.icons.SAVE, on_click=upload_configuration_file),
                    self.SidebarIcon(ft.icons.BAR_CHART),
                    self.SidebarIcon(ft.icons.HELP),
                    self.SidebarIcon(ft.icons.RESTART_ALT),
                    self.SidebarIcon(ft.icons.SETTINGS),
                ],
                # expand=True,
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            bgcolor=config.SIDEBAR_COLOR,
            padding=5,
        )

    class SidebarIcon(ft.IconButton):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.icon_color = config.SIDEBAR_ICONS_COLOR
