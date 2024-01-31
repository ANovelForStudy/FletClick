import os
import sys
from collections import deque
from enum import Enum, unique
from typing import Optional, Union

# Объявление типов
DelayValueType = Union[float, int]

#
# НАСТРОЙКИ ПРОГРАММЫ
#

VERSION = "0.1.0"

DEVELOPER = "anovelforstudy"

#
# НАСТРОЙКИ ОКНА
#

TITLE = "Flet Clicker"

# Размеры окна
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 360
SWITCH_SIZES = True

if SWITCH_SIZES:
    WINDOW_HEIGHT, WINDOW_WIDTH = WINDOW_WIDTH, WINDOW_HEIGHT

#
# СТАНДАРТНЫЕ НАСТРОЙКИ ФУНКЦИОНАЛА
#

# Значение на кнопках изменения значения погрешности рандомизации
DEFAULT_INACCURACY_CHANGE_VALUE: DelayValueType = 0.05
DEFAULT_INACCURACY_VALUE: DelayValueType = 0.5

# Значение на кнопках изменения значения задержки между нажатиями
DEFAULT_DELAY_BETWEEN_CLICKS_CHANGE_VALUE: DelayValueType = 0.05
DEFAULT_DELAY_BETWEEN_CLICKS_VALUE: DelayValueType = 0.1

# Значение задержки перед активацией кликера
DEFAULT_DELAY_VALUE_BEFORE_CLICKER_START: DelayValueType = 0.5

#
#  PAGE SETTINGS
#


# Перечисление для удобного выбора страницы по умолчанию
@unique
class Pages(Enum):
    main_clicker_settings_page = 0
    additional_clicker_settings_page = 1
    program_settings_page = 2


# Page padding
PAGE_PADDING_RIGHT = 0
PAGE_PADDING_LEFT = 0
PAGE_PADDING_TOP = 0
PAGE_PADDING_BOTTOM = 0

#
# НАСТРОЙКИ БЛОКОВ ИНТЕРФЕЙСА
#

# Стандартный отступ внутри блока
DEFAULT_BLOCK_PADDING = 5

# Боковая панель
SIDEBAR_ICONS_COLOR = "white"

#
# ЦВЕТА
#

# SIDEBAR_COLOR = "#171717"
SIDEBAR_COLOR = "#2A2A2A"

TOPBAR_COLOR = "#2A2A2A"

STATUSBAR_COLOR = "#2A2A2A"

#
# ФУНКЦИИ КОНФИГУРАЦИИ
#


def add_main_directory_to_path(verbose: Optional[bool] = False) -> None:
    """Adds a directory with the configuration file to PYTHONPATH

    Params:
        verbose (bool, optional): Turns on detailed function output. Useful for debugging. By default, False.
    """

    main_directory = os.path.dirname(__file__)

    deque(sys.path).appendleft(main_directory)
