import tkinter as tk

def calculate_ci():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get()) / 100
    years = float(years_entry.get())
    
    amount = principal * (1 + rate) ** years
    ci = amount - principal
    ci_text.set(round(ci, 2))

def clear_entries():
    principal_entry.delete(0, tk.END)
    rate_entry.delete(0, tk.END)
    years_entry.delete(0, tk.END)
    ci_text.set("")

window = tk.Tk()
window.title("Compound Interest Calculator")

# Labels
principal_label = tk.Label(window, text="Principal amount")
principal_label.grid(row=0, column=0, padx=10, pady=5)

rate_label = tk.Label(window, text="Rate of interest")
rate_label.grid(row=1, column=0, padx=10, pady=5)

years_label = tk.Label(window, text="Number of years")
years_label.grid(row=2, column=0, padx=10, pady=5)

ci_label = tk.Label(window, text="Compound interest")
ci_label.grid(row=3, column=0, padx=10, pady=5)

# Entry fields
principal_entry = tk.Entry(window)
principal_entry.grid(row=0, column=1)

rate_entry = tk.Entry(window)
rate_entry.grid(row=1, column=1)

years_entry = tk.Entry(window)
years_entry.grid(row=2, column=1)

ci_text = tk.StringVar()
ci_text.set("")
ci_entry = tk.Entry(window, textvariable=ci_text, state="readonly")
ci_entry.grid(row=3, column=1)

# Buttons
calculate_button = tk.Button(window, text="Calculate", command=calculate_ci)
calculate_button.grid(row=4, column=0, padx=10, pady=5)

clear_button = tk.Button(window, text="Clear", command=clear_entries)
clear_button.grid(row=4, column=1, padx=10, pady=5)

window.mainloop()