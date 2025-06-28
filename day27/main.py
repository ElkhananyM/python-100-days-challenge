from tkinter import *


def button_clicked():
    my_label.config(text=input.get())


window = Tk()
window.title("Shiro's GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I Am a Label", font=("Courier", 18))
my_label["text"] = "New Text"
my_label.config(text="New New Text")
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button_2 = Button(text="New Button", command=button_clicked)
button_2.grid(column=2, row=0)
# Entry
input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()
