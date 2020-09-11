import pyautogui
import keyboard
import time
import sys
start = time.time()
elapsed = 0
run = True
while run:
    elapsed = time.time() - start
    print (elapsed)
    pyautogui.press('w')
    time.sleep(1)
    pyautogui.click()
    time.sleep(3)
    if elapsed > 10:
        sys.exit()
    if keyboard.is_pressed("Esc"):
        sys.exit()

