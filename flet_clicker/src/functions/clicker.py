import multiprocessing
from time import sleep

import pyautogui
from flet import ControlEvent
from icecream import ic


class Clicker:
    def __init__(self):
        self.clicking_process = None

    def _clicker(self):
        sleep(1.5)
        while True:
            pyautogui.click()
            sleep(0.1)

    def start_clicker(self, e: ControlEvent = None):
        self.clicking_process = multiprocessing.Process(target=self._clicker)
        self.clicking_process.start()
        ic("Процесс запущен")

    def stop_clicker(self, e: ControlEvent = None):
        if self.clicking_process is not None and self.clicking_process.is_alive():
            self.clicking_process.terminate()
            ic("Процесс прерван")
            self.clicking_process = None
        else:
            ic("Процесс не запущен")
