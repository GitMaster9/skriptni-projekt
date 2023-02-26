from tkinter import *

class ButtonStation:
    def __init__(self, master, station_info, function_to_start):
        self.master = master
        self.station_info = station_info

        self.button_to_display = Button(self.master, text=self.station_info.get("name"), command=lambda: function_to_start(self.station_info.get("url")))
        self.button_to_display.pack(fill=BOTH)