import pyautogui as pyauto
import time as t

user = 'U05SD21M00'

t.sleep(3)
#print(pyauto.position())

for i in range(50, 100):
    t.sleep(0.8)
    #username
    pyauto.moveTo(749, 405)
    pyauto.click(749, 405)
    pyauto.hotkey('ctrl', 'a')
    pyauto.hotkey('ctrl', 'x')
    t.sleep(0.2)
    pyauto.typewrite(user+str(i))

    t.sleep(0.8)

    '''#password
    pyauto.moveTo(700, 442)
    pyauto.click(700, 442)

    t.sleep(0.5)'''

    #login
    pyauto.moveTo(953, 530)
    pyauto.click(953, 530)

    t.sleep(1.5)
    #wrongPass
    pyauto.moveTo(1116, 200, duration=0.3)
    pyauto.click(1116, 200)
    
    