from enum import Enum, unique
from typing import List

import flet as ft

import config
from common.observer import Observer, Subject
from common.singleton import Singleton
from gui.controls.container_without_indents import ContainerWithoutIndents


# Перечисление, содержащее типы кликов
@unique
class TypeOfClicks(Enum):
    single_click = 1
    double_click = 2
    triple_click = 3


class SelectingTypeOfClicks(ft.UserControl, Singleton, Subject):
    """
    Класс (синглтон).
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Текущий выбранный режим кликов. По умолчанию одиночные клики
        self._current_clicks_type: int = TypeOfClicks.single_click

        # Список подписчиков
        self._observers: List[Observer] = []

    #
    # РЕАЛИЗАЦИЯ ПАТТЕРНА "НАБЛЮДАТЕЛЬ"
    #

    def add_observer(self, observer: Observer) -> None:
        print(f"[INFO] {self.__class__.__name__} : Наблюдатель {observer} подписался на уведомления")
        print(self._observers)
        self._observers.append(observer)
        print(self._observers)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        print(f"[INFO] {self.__class__.__name__} : Производится оповещение наблюдателей:")
        print(self._observers)
        if len(self._observers) == 0:
            print("Наблюдателей нет!")
        for observer in self._observers:
            print(f"...[INFO] Наблюдатель {observer} был оповещён")
            observer.update(self.current_clicks_type, self)

    #
    # СВОЙСТВА
    #

    @property
    def current_clicks_type(self) -> int:
        return self._current_clicks_type

    @current_clicks_type.setter
    def current_clicks_type(self, value: int) -> None:
        self._current_clicks_type = value
        # Уведомить наблюдателей
        self.notify_observers()

    #
    # ОБРАБОТЧИКИ СОБЫТИЙ
    #

    def set_current_clicks_type(self, e: ft.ControlEvent) -> None:
        """
        Обработчик RadioGroup. Реагирует на переключение CupertinoRadio
        """
        self.current_clicks_type = self._radio_group_selecting_clicks_type.value

    #
    # ПОСТРОЕНИЕ ИНТЕРФЕЙСА
    #

    def build(self):
        self._radio_single_click = ft.CupertinoRadio(
            value=TypeOfClicks.single_click,
        )

        self._radio_double_click = ft.CupertinoRadio(
            value=TypeOfClicks.double_click,
        )

        self._radio_triple_click = ft.CupertinoRadio(
            value=TypeOfClicks.triple_click,
        )

        self._radio_group_selecting_clicks_type = ft.RadioGroup(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            self._radio_single_click,
                            ft.Text("Одиночный"),
                        ],
                        spacing=3,
                    ),
                    ft.Row(
                        controls=[
                            self._radio_double_click,
                            ft.Text("Двойной"),
                        ],
                        spacing=3,
                    ),
                    ft.Row(
                        controls=[
                            self._radio_triple_click,
                            ft.Text("Тройной"),
                        ],
                        spacing=3,
                    ),
                ],
                spacing=1,
            ),
            # Значение по умолчанию
            value=TypeOfClicks.single_click,
            # События
            on_change=self.set_current_clicks_type,
        )

        return ContainerWithoutIndents(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value="ТИП НАЖАТИЙ".upper(),
                        font_family="Inter",
                    ),
                    self._radio_group_selecting_clicks_type,
                ],
                spacing=0,
            ),
            padding=config.DEFAULT_BLOCK_PADDING,
        )
