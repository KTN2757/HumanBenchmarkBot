import pyautogui
import keyboard
import win32api, win32con
import time

# FAILSAFE, just in case
pyautogui.FAILSAFE = True


# win32 click function(faster than pyautogui.click/doubleclick)
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# Defining the ONLY clickable color (slight green)
clickableColor = (75, 219, 106)

# Infinite loop to check the mouse's position and the color at the position
while keyboard.is_pressed("q") == False:
    x, y = pyautogui.position()
    hoveredColor = pyautogui.pixel(x, y)

    # Check if mouse is hovering over the clickable color
    if hoveredColor == clickableColor:
        # Looping left the chat
        click(x, y)
        click(x, y)
