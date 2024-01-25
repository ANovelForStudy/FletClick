import flet as ft
from util.get_random_color_name import get_random_color_name


class LabelContainer(ft.Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.padding is None:
            self.padding = ft.Padding(
                left=4,
                right=4,
                top=0,
                bottom=0,
            )

        # Изменение цвета контейнера на случайный (для отладки)
        if self.bgcolor is None:
            self.bgcolor = get_random_color_name()

        if self.expand is None:
            self.expand = True
