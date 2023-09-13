from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def miles_to_km():
    miles = float(input_mil.get())
    km = round(miles * 1.609)
    km_label.config(text=f"{km}")


mil = Label(text="Miles")
mil.grid(column=2, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)

equal_to = Label(text="is equal to")
equal_to.grid(column=0, row=1)

input_mil = Entry(width=7)
input_mil.grid(column=1, row=0)

km_label = Label(text="0")
km_label.grid(column=1, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()