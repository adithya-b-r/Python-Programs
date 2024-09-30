import pyautogui as auto
import time as t

no_of_msg = int(input("Enter number of msgs : "))
msg = input("Enter your msg : ")

for i in range(1,6):
    t.sleep(1)
    print(f"Starting in {i} ...")

for n in range(0, no_of_msg):
    auto.write(msg)
    auto.press("enter")
    t.sleep(.3)
    print("Number of messages :",n)

print("Script excecuted successfully! :)")
