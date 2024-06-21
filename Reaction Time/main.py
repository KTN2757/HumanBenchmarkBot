"""Requirements."""
import time
import pyautogui
import keyboard
import win32api
import win32con

# FAILSAFE, just in case
pyautogui.FAILSAFE = True


# win32 click function(faster than pyautogui.click/doubleclick)
def click(x, y):
    """Clicks."""
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


CLICKABLE_COLOR = (75, 219, 106)
COUNT = 0

while not keyboard.is_pressed("q"):
    if COUNT < 5:
        if pyautogui.pixel(200, 200) == CLICKABLE_COLOR:
            click(200, 200)
            click(200, 200)
            COUNT += 1
    else:
        # Gotta wait till it loads.
        time.sleep(1)
        click(723, 575)
        click(200, 200)
        COUNT = 0
