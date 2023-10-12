import pyautogui
import time
import keyboard
import win32api, win32con

# bottom left = 185, 662 RGB:(43, 135, 209)
# top right = 1219, 207 RGB(43, 135, 209)
# gray = (149, 195, 232) = (29, 67, 97)
# X: 117, Y:188, Right: 1172, Bottom:727, Width 996, Height:540

pyautogui.FAILSAFE = True
print(pyautogui.size())
time.sleep(1)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed("q") == False:
    window = pyautogui.screenshot(region=(117, 188, 1172, 540))
    w, h = window.size
    for x in range(0, w, 5):
        for y in range(0, h, 5):
            r, g, b = window.getpixel((x, y))
            if r == 29:
                click(x + 117, y + 188)
                break
