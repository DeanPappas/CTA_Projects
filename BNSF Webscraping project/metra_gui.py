from tkinter import *
from tkinter.ttk import Combobox

class metra_GUI:
    def __init__(self, metra_data):
        self.metra_data = metra_data

        # Init window
        self.window = Tk()
        self.window.title("BNSF Tracker")
        # Init Labels
        self.train_num = Label(self.window, text="")
        self.train_num.grid(row=0, column=0)
        self.departure_time = Label(self.window, text="")
        self.departure_time.grid(row=1, column=0)
        self.arrival_time = Label(self.window, text="")
        self.arrival_time.grid(row=2, column=0)
        self.init_data()
        self.window.mainloop()



    def init_data(self):
        train_nums = []
        departure_times = []
        arrival_times = []
        for x in self.metra_data:
            train_nums.append(f"Train: {x}")
            print(self.metra_data)
            departure_times.append(f"Departure Time: {self.metra_data[x][0]}")
            arrival_times.append(f"Arrival Time: {self.metra_data[x][1]}")

            self.train_num.config(text=train_nums[0])
            self.departure_time.config(text=departure_times[0])
            self.arrival_time.config(text=arrival_times[0])

        # print(departure_times)
        # print(arrival_times)