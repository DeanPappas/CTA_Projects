from tkinter import *
from tkinter.ttk import Combobox

class metra_GUI:
    def __init__(self, metra_times):
        self.metra_data = metra_times

        # Init window
        self.window = Tk()
        self.window.title("BNSF Tracker")