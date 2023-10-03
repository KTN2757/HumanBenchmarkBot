import pyautogui
import time

# FAILSAFE, just in case
pyautogui.FAILSAFE = True

# Defining the ONLY clickable color (white)
clickableColor = (255, 255, 255)

# Positions of Tiles
x = [558, 652, 812, 540, 669, 816, 520, 699, 798]
y = [346, 342, 353, 486, 486, 485, 609, 618, 613]

# Infinitely Iterating Loop
i = 0
while True:
    if pyautogui.pixel(x[i], y[i]) == clickableColor:
        pyautogui.click(x[i], y[i])
    i += 1
    if i == 9:
        i = 0
