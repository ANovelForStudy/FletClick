import flet as ft

import config
from gui.controls.container_without_indents import ContainerWithoutIndents


class SelectingDelayBetweenClicks(ft.UserControl):
    """
    Класс отвечает отрисовку и обработку событий блока управления задержкой между нажатиями.

    Поля:
        self._last_correct_delay_value (float): Последнее корректное значение из текстового поля ввода
            значения задержки между нажатиями self._text_field_delay_between_clicks.
            При запуске приложения инициализируется значением DEFAULT_DELAY_BETWEEN_CLICKS_VALUE, указанным в
            конфигурационном файле.

        self._current_delay_value (str): Текущее значение из текстового поля ввода
            значения задержки между нажатиями self._text_field_delay_between_clicks.
            Изменяется при потере полем фокуса или при нажатии клавиши Enter во время ввода.
            При запуске приложения инициализируется пустой строкой.
    """

    _instance = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._last_correct_delay_value: float = config.DEFAULT_DELAY_BETWEEN_CLICKS_VALUE
        self._current_delay_value: str = ""

        self._observers = []

    def __new__(cls, *args, **kwargs):
        # Реализация паттерна "Синглтон"
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        print(hex(id(cls._instance)))
        return cls._instance

    #
    # РЕАЛИЗАЦИЯ ПАТТЕРНА "НАБЛЮДАТЕЛЬ"
    #

    # Добавить наблюдателя
    def add_observer(self, observer):
        self._observers.append(observer)

    # Удалить наблюдателя
    def remove_observer(self, observer):
        self._observers.remove(observer)

    # Уведомить наблюдателей
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self.last_correct_delay_value)

    #
    # СВОЙСТВА
    #

    @property
    def last_correct_delay_value(self):
        return self._last_correct_delay_value

    @last_correct_delay_value.setter
    def last_correct_delay_value(self, value):
        self._last_correct_delay_value = value
        # Уведомить наблюдателей
        self.notify_observers()

    @property
    def current_delay_value(self):
        return self._current_delay_value

    #
    # ОБРАБОТКА СОБЫТИЙ
    #

    # Обработка событий кнопок изменения значения задержки между кликами
    def decrease_delay_value_between_clicks(self, e: ft.ControlEvent) -> None:
        """
        Метод уменьшает значение задержки между кликами на стандартную величину изменения,
        указанную в конфигурационном файле, иначе устанавливает последнее корректное значение
        """
        value: float = self.last_correct_delay_value
        new_value: float = round(value - config.DEFAULT_DELAY_BETWEEN_CLICKS_CHANGE_VALUE, 3)

        # Устанавливаем в поля ввода задержки и последнего корректного значения новое значение
        # Дополнительная проверка на то, что при уменьшении значения, оно не станет меньше или равно нулю
        if new_value > 0:
            self._text_field_delay_between_clicks.value = new_value
            self.last_correct_delay_value = new_value
            self._text_field_delay_between_clicks.update()

    def increase_delay_value_between_clicks(self, e: ft.ControlEvent) -> None:
        """
        Метод увеличивает значение задержки между кликами на стандартную величину изменения,
        указанную в конфигурационном файле, иначе устанавливает последнее корректное значение
        """
        value: float = self.last_correct_delay_value
        new_value: float = round(value + config.DEFAULT_DELAY_BETWEEN_CLICKS_CHANGE_VALUE, 3)

        # Устанавливаем в поля ввода задержки и последнего корректного значения новое значение
        self._text_field_delay_between_clicks.value = new_value
        self.last_correct_delay_value = new_value
        self._text_field_delay_between_clicks.update()

    def reset_delay_value_between_clicks(self, e: ft.ControlEvent) -> None:
        """
        Метод устанавливает значение задержки между кликами в поле и в экземпляре класса на стандартное значение,
        указанное в конфигурационном файле
        """
        self.last_correct_delay_value = config.DEFAULT_DELAY_BETWEEN_CLICKS_VALUE
        self._text_field_delay_between_clicks.value = self.last_correct_delay_value
        self._text_field_delay_between_clicks.update()

    # Обработка событий поля ввода значения задержки между нажатиями
    def check_delay_value_is_correct(self) -> bool:
        """
        Метод проверяет введённое значение задержки между нажатиями. Проверка выполняется за счёт обработки исключения,
        которое может возникнуть при попытке приведения типа значения из поля к типу float. Также проверяется, что
        число будет больше нуля (задержка не может быть ниже или равна нулю)
        """
        try:
            value_to_check = float(self._current_delay_value)
            if value_to_check <= 0:
                return False
        except ValueError:
            return False

        return True

    def save_current_delay_value(self) -> None:
        """
        Метод сохраняет текущее введённое значение задержки между нажатиями и устанавливает его в поле self._current_inaccuracy_value,
        а также заменяет в нём запятые на точки для удобства дальнейшей обработки и предоставления возможности использования запятой в качестве отделителя дробной части числа
        """
        self._current_delay_value = str(self._text_field_delay_between_clicks.value).replace(",", ".")

    def save_last_correct_delay_value(self) -> None:
        """
        Метод сохраняет текущее значение задержки между нажатиями из поля self._current_delay_value
        как последнее корректное значение задержки между нажатиями, приведя его к типу float
        """
        self.last_correct_delay_value = float(self._current_delay_value)

    def set_last_correct_delay_value_in_field(self) -> None:
        """
        Метод устанавливает последнее корректное значение задержки между нажатиями в поле ввода в том случае,
        если текущее введённое пользователем значение оказывается некорректным
        """
        self._text_field_delay_between_clicks.value = self.last_correct_delay_value

        self._text_field_delay_between_clicks.update()

    def text_field_delay_between_clicks_handler(self, e: ft.ControlEvent) -> None:
        """
        Метод-обработчик текстового поля ввода значения задержки между кликами
        """
        # Сохранить текущее значение поля в экземпляре класса
        self.save_current_delay_value()
        # Если текущее значение корректно
        if self.check_delay_value_is_correct():
            # Сохранить текущее значение в качестве последнего введённого корректного значения
            self.save_last_correct_delay_value()
        else:
            # Иначе записать в поле последнее корректное значение
            self.set_last_correct_delay_value_in_field()

    #
    # ПОСТРОЕНИЕ ИНТЕРФЕЙСА
    #

    def build(self):
        self._text_button_decrease = ft.TextButton(
            text=f"-{config.DEFAULT_DELAY_BETWEEN_CLICKS_CHANGE_VALUE}",
            # События
            on_click=self.decrease_delay_value_between_clicks,
        )

        self._text_button_increase = ft.TextButton(
            text=f"+{config.DEFAULT_DELAY_BETWEEN_CLICKS_CHANGE_VALUE}",
            # События
            on_click=self.increase_delay_value_between_clicks,
        )

        self._text_field_delay_between_clicks = ft.TextField(
            value=config.DEFAULT_DELAY_BETWEEN_CLICKS_VALUE,
            width=140,
            height=35,
            content_padding=ft.Padding(
                left=10,
                right=10,
                bottom=3,
                top=3,
            ),
            label="Задержка",
            label_style=ft.TextStyle(font_family="Inter", size=14),
            # События
            on_blur=self.text_field_delay_between_clicks_handler,
            on_submit=self.text_field_delay_between_clicks_handler,
        )

        return ContainerWithoutIndents(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value="ЗАДЕРЖКА МЕЖДУ НАЖАТИЯМИ".upper(),
                        font_family="Inter",
                    ),
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    self._text_button_decrease,
                                    self._text_field_delay_between_clicks,
                                    self._text_button_increase,
                                ],
                                spacing=5,
                            ),
                            ft.Row(
                                controls=[
                                    ft.TextButton(
                                        text="Сбросить значение задержки",
                                        on_click=self.reset_delay_value_between_clicks,
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
