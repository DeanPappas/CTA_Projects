from tkinter import *
from tkinter.ttk import Combobox

window = Tk()

kimball_stops = Combobox(window, values=["No stops"])
# kimball_stops.configure(values=["test", "test"])
kimball_stops.current(0)
kimball_stops.grid(row=0, column=0, padx=20, pady=20)
window.mainloop()