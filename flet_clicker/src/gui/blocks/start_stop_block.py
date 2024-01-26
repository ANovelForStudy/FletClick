import flet as ft


class StartStopBlock(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        self._start_button = ft.ElevatedButton(
            text="Старт",
            width=120,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.GREEN,
            icon=ft.icons.PLAY_ARROW_ROUNDED,
        )

        self._stop_button = ft.ElevatedButton(
            text="Стоп",
            width=120,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.RED,
            icon=ft.icons.STOP_ROUNDED,
        )

        return ft.Container(
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
            margin=0,
            padding=5,
            scale=1,
        )
