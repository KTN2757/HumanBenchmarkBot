# Works only when the website is in darkmode with the dark reader plugin.

"""Requirements."""
import time
import pyautogui
import keyboard
import win32api
import win32con
pyautogui.FAILSAFE = True
time.sleep(1)


def click(x, y):
    """Clicks."""
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while not keyboard.is_pressed("q"):
    window = pyautogui.screenshot(region=(198, 212, 1167, 675))
    w, h = window.size
    for x in range(0, w, 41):
        for y in range(0, h, 41):
            r, g, b = window.getpixel((x, y))
            if r == 29:
                click(x + 198, y + 212)
                break
