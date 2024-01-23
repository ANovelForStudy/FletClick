import flet as ft

import config


class Sidebar(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        return ft.Container(
            ft.Column(
                controls=[
                    self.SidebarIcon(ft.icons.UPLOAD_FILE),
                    self.SidebarIcon(ft.icons.SAVE),
                    self.SidebarIcon(ft.icons.BAR_CHART),
                    self.SidebarIcon(ft.icons.HELP),
                    self.SidebarIcon(ft.icons.RESTART_ALT),
                    self.SidebarIcon(ft.icons.SETTINGS),
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            bgcolor=ft.colors.BLACK87,
            padding=5,
            # expand=True,
            # alignment=ft.alignment.center,
        )

    class SidebarIcon(ft.IconButton):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.icon_color = config.SIDEBAR_ICONS_COLOR
            self.bgcolor = ft.colors.RED
