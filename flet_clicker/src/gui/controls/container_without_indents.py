import flet as ft
from util.get_random_color_name import get_random_color_name


class ContainerWithoutIndents(ft.Container):
    def __init__(self, *args, debug: bool = False, **kwargs):
        super().__init__(*args, **kwargs)

        if self.padding is None:
            self.padding = 0

        if self.margin is None:
            self.margin = 0

        # Изменение цвета контейнера на случайный (для отладки)
        if debug:
            self.bgcolor = get_random_color_name()
