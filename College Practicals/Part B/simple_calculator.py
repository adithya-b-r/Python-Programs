import tkinter as tk

def btn_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "ERROR")

window = tk.Tk()
window.title("SIMPLE CALCULATOR")

entry = tk.Entry(window, width=40, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4)

btns = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("%", 4, 0), ("0", 4, 1), (".", 4, 2), ("+", 4, 3)
]

for btn in btns:
    text, row, col = btn
    btn = tk.Button(window, text=text, width=7, height=1, command=lambda text=text: btn_click(text))
    btn.grid(row=row, column=col)

clear_btn = tk.Button(window, text="C", width=25, height=1, command=clear)
clear_btn.grid(row=5, column=0, columnspan=3)

equal_btn = tk.Button(window, text="=", width=7, height=1, command=equal)
equal_btn.grid(row=5, column=3)

window.mainloop()