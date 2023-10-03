import pyautogui

# FAILSAFE, just in case
pyautogui.FAILSAFE = True

# Defining the ONLY clickable color (slight green)
clickableColor = (75, 219, 106)

# Infinite loop to check the mouse's position and the color at the position
while True:
    x, y = pyautogui.position()
    hoveredColor = pyautogui.pixel(x, y)

    # Check if mouse is hovering over the clickable color
    if hoveredColor == clickableColor:
        pyautogui.doubleClick()
