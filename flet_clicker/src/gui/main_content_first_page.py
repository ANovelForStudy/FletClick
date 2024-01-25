import flet as ft
from icecream import ic

import config


class MainContentFirst(ft.UserControl):
    """Класс, строящий основное наполнение первой вкладки приложения"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            RandomizingTimeBetweenTaps(),
                            # ft.VerticalDivider(),
                            GuiStartStopButtons(),
                        ],
                        spacing=3,
                    ),
                    ft.Row(
                        controls=[
                            ClickerMode(),
                        ],
                        spacing=3,
                    ),
                ],
                spacing=0,
            ),
            margin=0,
            padding=0,
            expand=True,
            # bgcolor="yellow",
        )


class ClickerMode(ft.UserControl):
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


class RandomizingTimeBetweenTaps(ft.UserControl):
    """
    Класс отвечает за отрисовку и обработку событий блока управления рандомизацией значения задержки между нажатиями.

    Поля:
        self._last_correct_inaccuracy_value (float): Последнее корректное значение из поля ввода погрешности self._inaccuracy_value_field.
            При запуске приложения инициализируется значением DEFAULT_INACCURACY_VALUE, указанным в конфигурационном файле.

        self._current_inaccuracy_value (str): Текущее значение из поля ввода погрешности self._inaccuracy_value_field.
            Изменяется при потере полем фокуса или при нажатии клавиши Enter во время ввода.
            При запуске приложения инициализируется пустой строкой.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._last_correct_inaccuracy_value: float = config.DEFAULT_INACCURACY_VALUE
        self._current_inaccuracy_value: str = ""

    #
    # СВОЙСТВА
    #

    @property
    def last_correct_inaccuracy_value(self):
        return self._last_correct_inaccuracy_value

    @property
    def current_inaccuracy_value(self):
        return self._current_inaccuracy_value

    #
    # ОБРАБОТКА СОБЫТИЙ
    #

    # Обработка событий кнопок изменения погрешности
    def increase_inaccuracy_value(self, e: ft.ControlEvent) -> None:
        """Метод увеличивает значение погрешности на значение изменения, указанное в конфигурационном файле,
        иначе устанавливает последнее корректное значение"""
        value: str = self._inaccuracy_value_field.value
        self._inaccuracy_value_field.value = round(float(value) + config.DEFAULT_INACCURACY_CHANGE_VALUE, 2)
        self._inaccuracy_value_field.update()

    def decrease_inaccuracy_value(self, e: ft.ControlEvent) -> None:
        """Метод уменьшает значение погрешности на значение изменения, указанное в конфигурационном файле,
        иначе устанавливает последнее корректное значение"""
        value: str = self._inaccuracy_value_field.value
        self._inaccuracy_value_field.value = round(float(value) - config.DEFAULT_INACCURACY_CHANGE_VALUE, 2)
        self._inaccuracy_value_field.update()

    # Обработка событий поля ввода значения погрешности
    def save_current_inaccuracy_value(self) -> None:
        """Метод сохраняет текущее введённое значение погрешности и устанавливает его в поле self._current_inaccuracy_value, а также заменяет в нём
        запятые на точки для удобства дальнейшей обработки и предоставления возможности использования запятой в качестве отделителя дробной части числа"""
        self._current_inaccuracy_value = str(self._inaccuracy_value_field.value).replace(",", ".")

    def check_value_is_correct(self, value: str) -> bool:
        """Метод проверяет введённое значение погрешности. Проверка выполняется за счёт обработки исключения,
        которое может возникнуть при попытке приведения типа значения из поля к типу float."""
        try:
            float(value)
            return True
        except ValueError:
            return False

    def save_last_correct_inaccuracy_value(self) -> None:
        """Метод сохраняет последнее конкретное значение погрешности, делая его доступным для восстановления
        в случае ввода некорректного значения в дальнейшем"""
        self._last_correct_inaccuracy_value = float(self._current_inaccuracy_value)

    def set_last_correct_inaccuracy_value_in_field(self) -> None:
        """Метод устанавливает последнее корректное значение погрешности в поле ввода в том случае, если
        текущее введённое пользователем значение оказывается некорректным"""
        self._inaccuracy_value_field.value = self._last_correct_inaccuracy_value
        self._inaccuracy_value_field.update()

    def inaccuracy_value_field_handler(self, e: ft.ControlEvent) -> None:
        # Сохранить текущее значение поля в экземпляре класса
        self.save_current_inaccuracy_value()
        # Если текущее значение корректно
        if self.check_value_is_correct(self._current_inaccuracy_value):
            # Сохранить текущее значение в качестве последнего введённого корректного значения
            self.save_last_correct_inaccuracy_value()
        else:
            # Иначе записать в поле последнее корректное значение
            self.set_last_correct_inaccuracy_value_in_field()

    #
    # ГРАФИЧЕСКИЙ ИНТЕРФЕЙС
    #

    def build(self):
        self._decrease_button = ft.TextButton(
            text=f"-{config.DEFAULT_INACCURACY_CHANGE_VALUE}",
            # События
            on_click=self.decrease_inaccuracy_value,
        )

        self._increase_button = ft.TextButton(
            text=f"+{config.DEFAULT_INACCURACY_CHANGE_VALUE}",
            # События
            on_click=self.increase_inaccuracy_value,
        )

        self._inaccuracy_value_field = ft.TextField(
            value=0.5,
            width=140,
            height=35,
            content_padding=ft.Padding(
                left=10,
                right=10,
                bottom=3,
                top=3,
            ),
            label="Погрешность",
            label_style=ft.TextStyle(font_family="Inter", size=14),
            # События
            on_blur=self.inaccuracy_value_field_handler,
            on_submit=self.inaccuracy_value_field_handler,
        )

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value="РАНДОМИЗАЦИЯ НАЖАТИЙ".upper(),
                        font_family="Inter",
                    ),
                    ft.Row(
                        controls=[
                            ft.CupertinoSwitch(scale=0.7),
                            ft.Text(
                                value="Включить рандомизацию",
                                font_family="Inter",
                            ),
                        ],
                        spacing=2,
                    ),
                    ft.Row(
                        controls=[
                            self._decrease_button,
                            self._inaccuracy_value_field,
                            self._increase_button,
                        ],
                        spacing=5,
                    ),
                ],
                spacing=2,
            ),
            margin=0,
            padding=5,
            scale=1,
            # bgcolor="red",
        )


class GuiStartStopButtons(ft.UserControl):
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
