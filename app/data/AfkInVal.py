import pyautogui
import time
while True:
    pyautogui.keyDown('s')
    time.sleep(.5)
    pyautogui.keyUp('s')
    time.sleep(1)