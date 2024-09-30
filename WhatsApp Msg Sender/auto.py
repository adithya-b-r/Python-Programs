import pyautogui as auto
import time as t

no_of_msg = int(input("Enter number of msgs : "))
msg = input("Enter your msg : ")

t.sleep(4)

for n in range(0, no_of_msg):
    auto.write(msg)
    auto.press("enter")

print("Script excecuted successfully! :)")