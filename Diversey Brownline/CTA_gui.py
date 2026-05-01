from tkinter import *
from tkinter.ttk import Combobox

class CTA_GUI:
    def __init__(self, CTA_times):
        self.CTA_data = CTA_times

        # Init window
        self.window = Tk()
        self.window.title("Diversey Tracker")
        self.window.iconbitmap("images/CTA.ico")
        # Images
        eva_img = PhotoImage(file="images/eva_line.png")
        diversey_img = PhotoImage(file="images/diversey.png")
        kimball_img = PhotoImage(file="images/kimball.png")
        loop_img = PhotoImage(file="images/loop.png")
        # BG Label
        self.bg_label = Label(self.window, image=eva_img)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # Buttons
        self.diversey_button = Button(self.window, image=diversey_img, highlightthickness=0, border=3, command=self.refresh_times)
        self.diversey_button.grid(row=0, column=0, columnspan=2, padx=30, pady=50)
        self.kimball_button = Button(self.window, image=kimball_img, highlightthickness=0, border=3, command=self.kimball_next_time)
        self.kimball_button.grid(row=1, column=0, padx=20, pady=20)
        self.loop_button = Button(self.window, image=loop_img, highlightthickness=0, border=3, command=self.loop_next_time)
        self.loop_button.grid(row=2, column=0, padx=20, pady=20)
        # Comboboxes
        self.kimball_stops = Combobox(self.window, values=[])
        self.kimball_stops.configure(font=("Arial", 20))
        self.kimball_stops.grid(row=1, column=1, padx=20, pady=20)
        self.loop_stops = Combobox(self.window, values=[])
        self.loop_stops.configure(font=("Arial", 20))
        self.loop_stops.grid(row=2, column=1,padx=20, pady=20)
        self.init_comboboxes()
        self.window.mainloop()

    def init_comboboxes(self):
        # Test for case where no kimball times are pulled from API
        try:
            self.kimball_stops.configure(values=self.CTA_data.kimball_stops)
            self.kimball_stops.set(self.CTA_data.kimball_stops[0])
        except IndexError:
            self.kimball_stops.configure(values=["No stops found"])
            self.kimball_stops.current(0)
        # Test for case where no loop times are pulled from API
        try:
            self.loop_stops.configure(values=self.CTA_data.loop_stops)
            self.loop_stops.set(self.CTA_data.loop_stops[0])
        except IndexError:
            self.loop_stops.configure(values=["No stops found"])
            self.loop_stops.current(0)

    def refresh_times(self):
        self.CTA_data.refresh_data()
        self.init_comboboxes()

    def kimball_next_time(self):
        selection = self.kimball_stops.current()
        try:
            self.kimball_stops.current(selection + 1)  # set the combobox to the next item
        except TclError:  # end of list reached
            self.kimball_stops.current(0)   # wrap around to first item

    def loop_next_time(self):
        selection = self.loop_stops.current()
        try:
            self.loop_stops.current(selection + 1)  # set the combobox to the next item
        except TclError:  # end of list reached
            self.loop_stops.current(0)   # wrap around to first item
