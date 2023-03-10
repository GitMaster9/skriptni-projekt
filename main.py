import sys
from tkinter import *

import stations
import modules.station_data as station_data
from modules.ButtonStation import ButtonStation
from modules.WindowStationInfo import WindowStationInfo

root = Tk()
root.protocol("WM_DELETE_WINDOW", sys.exit)
root.minsize(600, 500) # 960, 720
root.title('Usporedba meteoroloških postaja')

frameStationButtons1 = LabelFrame()
frameStationButtons2 = LabelFrame()
frameStationInfo = LabelFrame()
frameButtonBack = LabelFrame()

buttonStations = []

stations_all = stations.fetch_all_stations()

def open_station_in_new_window(requestURL):
    json_file = station_data.get_station_json_file(requestURL)
    new_window = WindowStationInfo(json_file, stations_all)

def set_station_buttons(stations):
    global frameStationButtons1
    global frameStationButtons2

    # inicijaliziranje
    frameStationButtons1 = LabelFrame(root, bd=0)
    frameStationButtons2 = LabelFrame(root, bd=0)

    # postavljanje u window
    frameStationButtons1.place(relx=0.35, rely=0.05, anchor=N)
    frameStationButtons2.place(relx=0.65, rely=0.05, anchor=N)

    global buttonStations
    buttonStations.clear()

    number_of_stations = len(stations)
    rows = (number_of_stations // 2) + (number_of_stations % 2)

    for i in range(number_of_stations):
        column = i // rows

        if column == 0: 
            btnNew = ButtonStation(frameStationButtons1, stations[i], open_station_in_new_window)
        else:
            btnNew = ButtonStation(frameStationButtons2, stations[i], open_station_in_new_window)

        buttonStations.append(btnNew)

stations_all = stations.fetch_all_stations()
set_station_buttons(stations_all)

mainloop()
