import pyautogui as a
import time as t

a.hotkey('win','r')
t.sleep(0.2)
a.write('cmd')
t.sleep(0.2)
a.press('enter')
t.sleep(1)
a.write('color a && dir/s')
t.sleep(1)
a.press('enter')
t.sleep(10)
a.hotkey('ctrl','c')
t.sleep(0.5)
a.write("exit")
t.sleep(0.2)
a.press('enter')