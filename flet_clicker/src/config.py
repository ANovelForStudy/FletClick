import os
import sys
from collections import deque
from enum import Enum, unique
from typing import Optional

#
# НАСТРОЙКИ ПРОГРАММЫ
#

# Версия программы для отображения
VERSION: str = "0.1.0"

# Разработчик программы
DEVELOPER: str = "anovelforstudy"

#
# НАСТРОЙКИ ОКНА
#

# Заголовок окна
TITLE: str = "Flet Clicker"

# Размеры окна
WINDOW_HEIGHT: int = 360
WINDOW_WIDTH: int = 500

#
# СТАНДАРТНЫЕ НАСТРОЙКИ ФУНКЦИОНАЛА
#

# Значение на кнопках изменения значения погрешности рандомизации
DEFAULT_INACCURACY_CHANGE_VALUE: float = 0.05
DEFAULT_INACCURACY_VALUE: float = 0.5

# Значение на кнопках изменения значения задержки между нажатиями
DEFAULT_DELAY_BETWEEN_CLICKS_CHANGE_VALUE: float = 0.01
DEFAULT_DELAY_BETWEEN_CLICKS_VALUE: float = 0.1

# Значение задержки перед активацией кликера
DEFAULT_DELAY_VALUE_BEFORE_CLICKER_START: float = 0.5

#
#  PAGE SETTINGS
#


# Перечисление для удобного выбора страницы по умолчанию
@unique
class Pages(Enum):
    main_clicker_settings_page = 0
    additional_clicker_settings_page = 1
    program_settings_page = 2


# Отступы на странице
PAGE_PADDING_RIGHT: int = 0
PAGE_PADDING_LEFT: int = 0
PAGE_PADDING_TOP: int = 0
PAGE_PADDING_BOTTOM: int = 0

#
# НАСТРОЙКИ БЛОКОВ ИНТЕРФЕЙСА
#

# Стандартный отступ внутри блока
DEFAULT_BLOCK_PADDING: int = 5

#
# ЦВЕТА
#

# Основная цветовая схема окна
COLOR_SCHEME_SEED = "blue"

# SIDEBAR_COLOR = "#171717"
SIDEBAR_COLOR: str = "#2A2A2A"
SIDEBAR_ICONS_COLOR: str = "white"

TOPBAR_COLOR: str = "#2A2A2A"

STATUSBAR_COLOR: str = "#2A2A2A"

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
