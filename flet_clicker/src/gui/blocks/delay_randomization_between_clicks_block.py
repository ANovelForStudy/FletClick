import flet as ft

import config
from gui.controls.container_without_indents import ContainerWithoutIndents


class DelayRandomizationBetweenClicksBlock(ft.UserControl):
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
        """
        Метод увеличивает значение погрешности на стандартную величину изменения,
        указанную в конфигурационном файле, иначе устанавливает последнее корректное значение
        """
        value: float = self._last_correct_inaccuracy_value
        new_value: float = round(value + config.DEFAULT_INACCURACY_CHANGE_VALUE, 2)
        # Устанавливаем в качестве нового значения поля ввода
        # погрешности и последнего корректного значения новый результат
        self._text_field_inaccuracy.value = new_value
        self._last_correct_inaccuracy_value = new_value
        self._text_field_inaccuracy.update()

    def decrease_inaccuracy_value(self, e: ft.ControlEvent) -> None:
        """
        Метод уменьшает значение погрешности на стандартную величину изменения,
        указанную в конфигурационном файле, иначе устанавливает последнее корректное значение
        """
        value: float = self._last_correct_inaccuracy_value
        new_value: float = round(value - config.DEFAULT_INACCURACY_CHANGE_VALUE, 2)
        # Устанавливаем в поля ввода погрешности и последнего корректного значения новое значение
        # Дополнительная проверка на то, что при уменьшении значения, оно не станет меньше или равно нулю
        if new_value > 0:
            self._text_field_inaccuracy.value = new_value
            self._last_correct_inaccuracy_value = new_value
            self._text_field_inaccuracy.update()

    def reset_inaccuracy_value(self, e: ft.ControlEvent) -> None:
        """
        Метод устанавливает значение погрешности в текстовом поле и в экземпляре класса на стандартное значение,
        указанное в конфигурационном файле
        """
        self._last_correct_inaccuracy_value = config.DEFAULT_INACCURACY_VALUE
        self._text_field_inaccuracy.value = self._last_correct_inaccuracy_value
        self._text_field_inaccuracy.update()

    # Обработка событий поля ввода значения погрешности
    def check_inaccuracy_value_is_correct(self) -> bool:
        """
        Метод проверяет введённое значение погрешности. Проверка выполняется за счёт обработки исключения,
        которое может возникнуть при попытке приведения типа значения из поля к типу float. Также проверяется, что
        число будет больше нуля (погрешность не может быть ниже или равна нулю)
        """
        try:
            value_to_check = float(self._current_inaccuracy_value)
            if value_to_check <= 0:
                return False
        except ValueError:
            return False

        return True

    def save_current_inaccuracy_value(self) -> None:
        """
        Метод сохраняет текущее введённое значение погрешности и устанавливает его в поле self._current_inaccuracy_value, а также заменяет в нём
        запятые на точки для удобства дальнейшей обработки и предоставления возможности использования запятой в качестве отделителя дробной части числа
        """
        self._current_inaccuracy_value = str(self._text_field_inaccuracy.value).replace(",", ".")

    def save_last_correct_inaccuracy_value(self) -> None:
        """
        Метод сохраняет текущее значение погрешности из поля self._current_inaccuracy_value
        как последнее корректное значение задержки между нажатиями, приведя его к типу float
        """
        self._last_correct_inaccuracy_value = float(self._current_inaccuracy_value)

    def set_last_correct_inaccuracy_value_in_field(self) -> None:
        """
        Метод устанавливает последнее корректное значение погрешности в поле ввода в том случае, если
        текущее введённое пользователем значение оказывается некорректным
        """
        self._text_field_inaccuracy.value = self._last_correct_inaccuracy_value

        self._text_field_inaccuracy.update()

    def text_field_inaccuracy_handler(self, e: ft.ControlEvent) -> None:
        # Сохранить текущее значение поля в экземпляре класса
        self.save_current_inaccuracy_value()
        # Если текущее значение корректно
        if self.check_inaccuracy_value_is_correct():
            # Сохранить текущее значение в качестве последнего введённого корректного значения
            self.save_last_correct_inaccuracy_value()
        else:
            # Иначе записать в поле последнее корректное значение
            self.set_last_correct_inaccuracy_value_in_field()

    #
    # ГРАФИЧЕСКИЙ ИНТЕРФЕЙС
    #

    def build(self):
        self._text_button_decrease = ft.TextButton(
            text=f"-{config.DEFAULT_INACCURACY_CHANGE_VALUE}",
            # События
            on_click=self.decrease_inaccuracy_value,
        )

        self._text_button_increase = ft.TextButton(
            text=f"+{config.DEFAULT_INACCURACY_CHANGE_VALUE}",
            # События
            on_click=self.increase_inaccuracy_value,
        )

        self._text_field_inaccuracy = ft.TextField(
            value=config.DEFAULT_INACCURACY_VALUE,
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
            on_blur=self.text_field_inaccuracy_handler,
            on_submit=self.text_field_inaccuracy_handler,
        )

        return ContainerWithoutIndents(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value="РАНДОМИЗАЦИЯ НАЖАТИЙ".upper(),
                        font_family="Inter",
                    ),
                    ft.Column(
                        controls=[
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
                                    self._text_button_decrease,
                                    self._text_field_inaccuracy,
                                    self._text_button_increase,
                                ],
                                spacing=5,
                            ),
                            ft.Row(
                                controls=[
                                    ft.TextButton(
                                        text="Сбросить значение погрешности",
                                        on_click=self.reset_inaccuracy_value,
                                        height=40,
                                    ),
                                ],
                                spacing=2,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=1,
                    ),
                ],
                spacing=2,
            ),
            padding=config.DEFAULT_BLOCK_PADDING,
        )
