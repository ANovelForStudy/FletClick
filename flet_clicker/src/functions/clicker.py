from time import sleep
from typing import Any, Optional

import multiprocess
import pyautogui
from flet import ControlEvent
from icecream import ic

import config
from common.observer import Observer, Subject
from gui.blocks.selecting_delay_between_clicks_block import SelectingDelayBetweenClicks
from gui.blocks.selecting_type_of_clicks_block import SelectingTypeOfClicks


class Clicker(Observer):
    def __init__(self):
        self._clicking_process: Optional[multiprocess.Process] = None
        self._selecting_delay_between_clicks_block = SelectingDelayBetweenClicks()
        self._selecting_type_of_clicks_block = SelectingTypeOfClicks()

        #
        # ПОДПИСКА НА СОБЫТИЯ
        #

        # Подписаться на изменение поля задержки между кликами в SelectingDelayBetweenClicks
        self._selecting_delay_between_clicks_block.add_observer(self)

        # Подписаться на изменение режима кликов
        self._selecting_type_of_clicks_block.add_observer(self)

        #
        # КОНФИГУРАЦИОННЫЕ ЗНАЧЕНИЯ КЛИКЕРА
        #

        # Стандартное значение берётся из конфигурационного файла
        self._delay_between_clicks_value: float = config.DEFAULT_DELAY_BETWEEN_CLICKS_VALUE
        # По умолчанию тип кликов равен типу, указанному в классе SelectingTypeOfClicks
        self._type_of_clicks: int = self._selecting_type_of_clicks_block.current_clicks_type

    #
    # РЕАЛИЗАЦИЯ ПАТТЕРНА "НАБЛЮДАТЕЛЬ"
    #

    def update(self, value: Any, subject: Subject) -> None:
        if subject is self._selecting_delay_between_clicks_block:
            # Реакция на изменение значения задержки между кликами
            self._delay_between_clicks_value: float = value
            print(f"[INFO] Current delay between clicks value : {self._delay_between_clicks_value}")

        if subject is self._selecting_type_of_clicks_block:
            # Реакция на изменение типа кликов
            print(str(value) + " - Well done")

    # def update_type_of_clicks(self, value: int) -> None:
    #     """
    #     Метод для реагирования на изменение типа кликов из класса SelectingTypeOfClicks
    #     """
    #     print(value, " Success")
    #     self._type_of_clicks: int = value

    def _clicker(self):
        # Установка задержки перед запуском кликера
        sleep(config.DEFAULT_DELAY_VALUE_BEFORE_CLICKER_START)

        while True:
            # Установка клика
            pyautogui.click()
            # Установка задержки между кликами
            sleep(self._delay_between_clicks_value)

    #
    # ОБРАБОТКА СОБЫТИЙ
    #

    def start_clicker(self, e: ControlEvent):
        """
        Метод запускает работу кликера

        Параметры:
            e (ControlEvent): Событие нажатия на кнопку Flet.
        """

        # Проверка на то, что процесс кликера не существует, чтобы не произошёл
        # запуск нескольких процессов кликера одновременно
        if self._clicking_process is None:
            # Создание процесса для работы кликера и его запись
            self._clicking_process = multiprocess.Process(target=self._clicker)
            # Запуск процесса
            self._clicking_process.start()

    def stop_clicker(self, e: ControlEvent):
        """
        Метод прерывает работу кликера

        Параметры:
            e (ControlEvent): Событие нажатия на кнопку Flet.
        """

        # Проверка на то, что процесс кликера существует
        if self._clicking_process is not None:
            # Остановка процесса
            self._clicking_process.terminate()
            # Установка переменной в None
            self._clicking_process = None
