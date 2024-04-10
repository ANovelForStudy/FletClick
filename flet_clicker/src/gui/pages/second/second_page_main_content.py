import flet as ft

from gui.blocks.delay_randomization_between_clicks_block import DelayRandomizationBetweenClicksBlock
from gui.blocks.selecting_click_location_block import SelectingClickLocationBlock
from gui.blocks.selecting_type_of_clicks_block import SelectingTypeOfClicks
from gui.controls.container_without_indents import ContainerWithoutIndents


class MainContentSecondPage(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        return ContainerWithoutIndents(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            SelectingClickLocationBlock(),
                            SelectingTypeOfClicks(),
                        ],
                        spacing=3,
                    ),
                    ft.Row(
                        controls=[
                            DelayRandomizationBetweenClicksBlock(),
                        ],
                        spacing=3,
                    ),
                ],
                spacing=0,
            ),
            expand=True,
        )
