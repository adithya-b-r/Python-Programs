import pyautogui as auto
import time as t

for i in range(1,6):
    t.sleep(1)
    print(f"Starting in {i} ...")

for n in range(0, 100):
    t.sleep(0.3)
    auto.press("enter")
