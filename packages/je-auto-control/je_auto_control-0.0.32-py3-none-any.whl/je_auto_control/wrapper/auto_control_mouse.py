import sys

from je_auto_control.utils.je_auto_control_exception import exception_tag
from je_auto_control.utils.je_auto_control_exception.exceptions import AutoControlCantFindKeyException
from je_auto_control.utils.je_auto_control_exception.exceptions import AutoControlMouseException
from je_auto_control.wrapper.auto_control_screen import size
from je_auto_control.wrapper.platform_wrapper import mouse
from je_auto_control.wrapper.platform_wrapper import mouse_table
from je_auto_control.wrapper.platform_wrapper import special_table


def position():
    try:
        return mouse.position()
    except Exception:
        raise AutoControlMouseException(exception_tag.mouse_get_position)


def set_position(x, y):
    try:
        mouse.set_position(x=x, y=y)
    except Exception:
        raise AutoControlMouseException(exception_tag.mouse_set_position)


def press_mouse(mouse_keycode, x=None, y=None):
    try:
        mouse_keycode = mouse_table.get(mouse_keycode)
    except Exception:
        raise AutoControlCantFindKeyException(exception_tag.table_cant_find_key)
    try:
        now_x, now_y = position()
        if x is None:
            x = now_x
        if y is None:
            y = now_y
        if sys.platform in ["win32", "cygwin", "msys", "linux", "linux2"]:
            mouse.press_mouse(mouse_keycode)
        elif sys.platform in ["darwin"]:
            mouse.press_mouse(x, y, mouse_keycode)
    except Exception:
        raise AutoControlMouseException(exception_tag.mouse_press_mouse)


def release_mouse(mouse_keycode, x=None, y=None):
    try:
        mouse_keycode = mouse_table.get(mouse_keycode)
    except Exception:
        raise AutoControlCantFindKeyException(exception_tag.table_cant_find_key)
    try:
        now_x, now_y = position()
        if x is None:
            x = now_x
        if y is None:
            y = now_y
    except Exception:
        raise AutoControlMouseException(exception_tag.mouse_get_position)
    try:
        if sys.platform in ["win32", "cygwin", "msys", "linux", "linux2"]:
            mouse.release_mouse(mouse_keycode)
        elif sys.platform in ["darwin"]:
            mouse.release_mouse(x, y, mouse_keycode)
    except Exception:
        raise AutoControlMouseException(exception_tag.mouse_release_mouse)


def click_mouse(mouse_keycode, x=None, y=None):
    try:
        mouse_keycode = mouse_table.get(mouse_keycode)
    except Exception:
        raise AutoControlCantFindKeyException(exception_tag.table_cant_find_key)
    try:
        now_x, now_y = position()
        if x is None:
            x = now_x
        if y is None:
            y = now_y
    except Exception:
        raise AutoControlMouseException(exception_tag.mouse_get_position)
    try:
        if sys.platform in ["win32", "cygwin", "msys", "linux", "linux2"]:
            mouse.click_mouse(mouse_keycode)
        elif sys.platform in ["darwin"]:
            mouse.click_mouse(x, y, mouse_keycode)
    except Exception:
        raise AutoControlMouseException(exception_tag.mouse_click_mouse)


def scroll(scroll_value, x=None, y=None, scroll_direction="scroll_down"):
    """"
    scroll_direction = 4 : direction up
    scroll_direction = 5 : direction down
    scroll_direction = 6 : direction left
    scroll_direction = 7 : direction right
    """
    try:
        now_cursor_x, now_cursor_y = position()
    except Exception:
        raise AutoControlMouseException(exception_tag.mouse_get_position)
    width, height = size()
    if x is None:
        x = now_cursor_x
    else:
        if x < 0:
            x = 0
        elif x >= width:
            x = width - 1
    if y is None:
        y = now_cursor_y
    else:
        if y < 0:
            y = 0
        elif y >= height:
            y = height - 1
    try:
        if sys.platform in ["win32", "cygwin", "msys"]:
            mouse.scroll(scroll_value, x, y)
        elif sys.platform in ["darwin"]:
            mouse.scroll(scroll_value)
        elif sys.platform in ["linux", "linux2"]:
            scroll_direction = special_table.get(scroll_direction)
            mouse.scroll(scroll_value, scroll_direction)
    except Exception:
        raise AutoControlMouseException(exception_tag.mouse_click_mouse)
