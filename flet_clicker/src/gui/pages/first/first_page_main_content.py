import flet as ft

from gui.blocks.selecting_clicker_mode_block import SelectingClickerModeBlock
from gui.blocks.selecting_delay_between_clicks_block import SelectingDelayBetweenClicks
from gui.blocks.start_stop_block import StartStopBlock
from gui.controls.container_without_indents import ContainerWithoutIndents


class MainContentFirstPage(ft.UserControl):
    """
    Класс, строящий основное наполнение первой вкладки приложения
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        return ContainerWithoutIndents(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            SelectingDelayBetweenClicks(),
                            # ft.VerticalDivider(),
                            StartStopBlock(),
                        ],
                        spacing=3,
                    ),
                    ft.Row(
                        controls=[
                            SelectingClickerModeBlock(),
                        ],
                        spacing=3,
                    ),
                ],
                spacing=0,
            ),
            expand=True,
            # bgcolor="yellow",
        )
