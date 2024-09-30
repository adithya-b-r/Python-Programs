from functools import total_ordering
from tkinter import *

window = Tk()
window.title("Window Title")
window.geometry("450x100")

label = Label(text = "Enter number : ")
entry_box = Entry (text = 0)

output_box = Message(text = 0)

output_box ["bg"] = "red"
output_box ["fg"] = "white"

output_box ["relief"] = "sunken"

list_box = Listbox()

entry_box ["justify"] = "center"

button1 = Button(text = "Click here", command = "click")

label.place(x = 50, y = 20, width = 100, height = 25)

total = 1
output_txt = 0
output_txt["text"] = str(total)
num = entry_box.get()
ans = output_txt["text"]

window.mainloop()