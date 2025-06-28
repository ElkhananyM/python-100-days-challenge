from tkinter import *

window = Tk()
window.config(padx=20, pady=20)
window.title("Shiro's Mile to Km Converter")

def convert_to_km():
    label_3.config(text=f"{float(input.get()) * 1.60934:.2f}")

input = Entry(width=7)
input.grid(column=1, row=0)
label_1 = Label(text="Miles", font=("Courier", 14))
label_1.grid(column=2, row=0)
label_2 = Label(text="is equal to", font=("Courier", 14))
label_2.grid(column=0, row=1)
label_3 = Label(text="0", font=("Courier", 14))
label_3.grid(column=1, row=1)
label_4 = Label(text="Km", font=("Courier", 14))
label_4.grid(column=2, row=1)
button = Button(text="Calculate", command=convert_to_km)
button.grid(column=1, row=2)


window.mainloop()
