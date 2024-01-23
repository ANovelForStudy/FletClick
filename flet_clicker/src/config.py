import os
import sys
from collections import deque
from typing import Optional

#
# PROGRAM SETTINGS
#
VERSION = "0.1.0"
DEVELOPER = "anovelforstudy"

#
# WINDOW SETTINGS
#

TITLE = "Flet Clicker"

# Window size
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 320
SWITCH_SIZES = True

if SWITCH_SIZES:
    WINDOW_HEIGHT, WINDOW_WIDTH = WINDOW_WIDTH, WINDOW_HEIGHT

# Page padding
PAGE_PADDING_RIGHT = 0
PAGE_PADDING_LEFT = 0
PAGE_PADDING_TOP = 0
PAGE_PADDING_BOTTOM = 0

#
# BLOCKS SETTINGS
#

# Sidebar
SIDEBAR_ICONS_COLOR = "white"

# Statusbar

# Topbar

#
# COLORS
#
SIDEBAR_COLOR = "#171717"
TOPBAR_COLOR = "#2A2A2A"
STATUSBAR_COLOR = "#2A2A2A"


# CONFIGURATIONS FUNCTIONS
def add_main_directory_to_path(verbose: Optional[bool] = False) -> None:
    """Adds a directory with the configuration file to PYTHONPATH

    Params:
        verbose (bool, optional): Turns on detailed function output. Useful for debugging. By default, False.
    """
    main_directory = os.path.dirname(__file__)
    deque(sys.path).appendleft(main_directory)
