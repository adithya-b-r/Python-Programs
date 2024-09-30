from tkinter import *
import random

def roll():
    msg = Message()
    num = random.randint(1,6)
    msg["text"] = str(num)
    msg.place(x=230, y=90)

window = Tk()
window.title("EX 125")
window.geometry("480x360")

titlbl = Label(text="Roll A Die")
titlbl["justify"] = "center"
titlbl.place(x=0, y=20, width=480)
btn = Button(text="Roll", command=roll)
btn.place(x=208, y=60, width=60)

window.mainloop()