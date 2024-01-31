from time import sleep

import multiprocess
import pyautogui
from flet import ControlEvent
from icecream import ic

import config
from gui.blocks.selecting_delay_between_clicks_block import SelectingDelayBetweenClicks


class Clicker:
    def __init__(self):
        self._clicking_process = None
        self._selecting_delay_between_clicks_block = SelectingDelayBetweenClicks()

        #
        # ПОДПИСКА НА СОБЫТИЯ
        #

        # Подписаться на изменение поля задержки между кликами в SelectingDelayBetweenClicks
        self._selecting_delay_between_clicks_block.add_observer(self)

        #
        # КОНФИГУРАЦИОННЫЕ ЗНАЧЕНИЯ КЛИКЕРА
        #

        # Стандартное значение берётся из конфигурационного файла
        self._selecting_delay_between_clicks_value = config.DEFAULT_DELAY_BETWEEN_CLICKS_VALUE

    #
    # РЕАЛИЗАЦИЯ ПАТТЕРНА "НАБЛЮДАТЕЛЬ"
    #

    def update(self, value):
        """
        Метод для реагирования на изменение последнего корректного значения задержки между кликами из класса SelectingDelayBetweenClicks
        """
        # Логика реакции на изменение значения
        self._selecting_delay_between_clicks_value = value

    def _clicker(self):
        # Установка задержки перед запуском кликера
        sleep(config.DEFAULT_DELAY_VALUE_BEFORE_CLICKER_START)
        while True:
            # Установка клика
            pyautogui.click()
            # Установка задержки между кликами
            sleep(self._selecting_delay_between_clicks_value)

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
