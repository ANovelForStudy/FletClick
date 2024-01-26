import flet as ft


class SelectingClickerModeBlock(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        self._content_padding_value = ft.Padding(
            left=10,
            right=10,
            bottom=3,
            top=3,
        )

        self._click_count_field = ft.TextField(
            value=10000,
            width=100,
            height=30,
            content_padding=self._content_padding_value,
            label="Клики",
            label_style=ft.TextStyle(font_family="Inter", size=14),
        )

        self._timer_field = ft.TextField(
            value=10,
            width=100,
            height=30,
            content_padding=self._content_padding_value,
            label="Время",
            label_style=ft.TextStyle(font_family="Inter", size=14),
        )

        self._period_size_dropdown = ft.Dropdown(
            width=80,
            height=30,
            content_padding=ft.Padding(
                left=10,
                right=10,
                bottom=3,
                top=3,
            ),
            value="сек.",
            options=[
                ft.dropdown.Option("сек."),
                ft.dropdown.Option("мин."),
            ],
        )

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value="РЕЖИМ РАБОТЫ КЛИКЕРА".upper(),
                        font_family="Inter",
                    ),
                    ft.RadioGroup(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.CupertinoRadio(
                                            value=1,
                                        ),
                                        ft.Text("Продолжать выполнение до ручной остановки"),
                                    ],
                                    spacing=3,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.CupertinoRadio(
                                            value=2,
                                        ),
                                        ft.Text("Выключить через N нажатий", width=200),
                                        self._click_count_field,
                                        ft.Text("нажатий"),
                                    ],
                                    spacing=3,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.CupertinoRadio(
                                            value=3,
                                        ),
                                        ft.Text("Выключить через время", width=200),
                                        self._timer_field,
                                        self._period_size_dropdown,
                                    ],
                                    spacing=3,
                                ),
                            ],
                        ),
                    ),
                ],
                spacing=4,
            ),
            # bgcolor="green",
            padding=5,
        )
