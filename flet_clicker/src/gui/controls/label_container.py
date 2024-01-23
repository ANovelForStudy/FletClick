import flet as ft


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

        if self.bgcolor is None:
            self.bgcolor = "green"

        if self.expand is None:
            self.expand = True
