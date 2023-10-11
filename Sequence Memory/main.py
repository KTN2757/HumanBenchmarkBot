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
clickCounter = 0


def click(x, y):
    pass


clickableTilesX = []
clickableTilesY = []
while True:
    if pyautogui.pixel(x[i], y[i]) == clickableColor:
        clickableTilesX.append(x[i])
        clickableTilesY.append(y[i])
        time.sleep(clickCounter + 2)
        for j in range(0, len(clickableTilesX) - 1):
            print(clickableTilesX[j], clickableTilesY[j])
        clickCounter += 1
    i += 1
    if i == 9:
        i = 0
