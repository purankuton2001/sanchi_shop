import time
import pyautogui

def click_image(img_path):
    while True:
        position = pyautogui.locateOnScreen(img_path,confidence=.8)
        if position is not None:
            time.sleep(0.5)
            pyautogui.click(position)
            break