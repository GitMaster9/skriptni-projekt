from tkinter import *
import geopy.distance as distance
import threading

from modules.WindowCompareStations import WindowCompareStations
from modules.WindowDetailedCompare import WindowDetailedCompare
import modules.station_data as station_data
import modules.threadStarter as threadStarter

thread_find_closest_stations = threading.Thread()

class WindowStationInfo:
    def __init__(self, json_file, stations_dict_all):
        self.json_file = json_file
        self.stations_dict_all = stations_dict_all
        self.max_number_of_stations_to_compare = 4

        self.top = Toplevel()
        self.top.minsize(700, 700)
        self.top.title('Meteorološka postaja')

        self.frame_name = LabelFrame(self.top)
        self.frame_stats_datetime = LabelFrame(self.top)
        self.frame_stats_placeholder = LabelFrame(self.top)
        self.frame_stats = LabelFrame(self.top)
        self.frame_compare1 = LabelFrame(self.top)
        self.frame_compare2 = LabelFrame(self.top)
        self.frame_button_compare = LabelFrame(self.top)

        self.frame_name.place(relx=0.5, rely=0.05, anchor=N)
        self.frame_stats_datetime.place(relx=0.5, rely=0.15, anchor=N)
        self.frame_stats_placeholder.place(relx=0.45, rely=0.2, anchor=N)
        self.frame_stats.place(relx=0.6, rely=0.2, anchor=N)
        self.frame_compare1.place(relx=0.4, rely=0.4, anchor=N)
        self.frame_compare2.place(relx=0.6, rely=0.4, anchor=N)
        self.frame_button_compare.place(relx=0.5, rely=0.7, anchor=N)

        self.get_all_station_data(self.json_file)
        self.display_station_info_placeholder()
        self.display_station_info()
        self.display_compare_list()

        global thread_find_closest_stations
        threadStarter.startThread(thread_find_closest_stations, self.find_closest_stations)

        self.top.mainloop()

    def get_all_station_data(self, json_file):
        self.station_info = station_data.get_station_info_from_json(json_file)

        self.name = self.station_info.get("name")
        self.url = self.station_info.get("url")
        self.lat = self.station_info.get("lat")
        self.lon = self.station_info.get("lon")
        self.datetime = self.station_info.get("datetime")
        self.temp = self.station_info.get("temp")
        self.heat = self.station_info.get("heat")
        self.rh = self.station_info.get("rh")
        self.press = self.station_info.get("press")
        self.wavg = self.station_info.get("wavg")
        self.precip = self.station_info.get("precip24")

        self.temp = str(self.temp) + " °C"
        self.heat = str(self.heat) + " °C"
        self.rh = str(self.rh) + "%"
        self.press = str(self.press) + " hPa"
        self.wavg = str(self.wavg) + " m/s"
        self.precip = str(self.precip) + " mm"

        self.stations_can_compare = []

        for station in self.stations_dict_all:
            current_name = station.get("name")
            if (current_name != self.name):
                self.stations_can_compare.append(station)

    def display_station_info_placeholder(self):
        self.reset_frame_by_name(self.frame_stats_placeholder)

        text1 = "Temperatura: "
        text2 = "Osjet temperature: "
        text3 = "Relativna vlažnost: "
        text4 = "Tlak zraka: "
        text5 = "Brzina vjetra: "
        text6 = "Oborine u posljednja 24h: "

        self.label_1 = Label(self.frame_stats_placeholder, text=text1)
        self.label_1.pack()

        self.label_2 = Label(self.frame_stats_placeholder, text=text2)
        self.label_2.pack()

        self.label_3 = Label(self.frame_stats_placeholder, text=text3)
        self.label_3.pack()

        self.label_4 = Label(self.frame_stats_placeholder, text=text4)
        self.label_4.pack()

        self.label_5 = Label(self.frame_stats_placeholder, text=text5)
        self.label_5.pack()

        self.label_6 = Label(self.frame_stats_placeholder, text=text6)
        self.label_6.pack()

    def display_station_info(self):
        self.reset_frame_by_name(self.frame_name)
        self.reset_frame_by_name(self.frame_stats)

        self.label_datetime = Label(self.frame_stats_datetime, text=self.datetime)
        self.label_datetime.pack()

        self.label_name = Label(self.frame_name, text=self.name)
        self.label_name.pack()

        self.label_temp = Label(self.frame_stats, text=self.temp)
        self.label_temp.pack()
        self.label_heat = Label(self.frame_stats, text=self.heat)
        self.label_heat.pack()
        self.label_rh = Label(self.frame_stats, text=self.rh)
        self.label_rh.pack()
        self.label_press = Label(self.frame_stats, text=self.press)
        self.label_press.pack()
        self.label_wavg = Label(self.frame_stats, text=self.wavg)
        self.label_wavg.pack()
        self.label_precip = Label(self.frame_stats, text=self.precip)
        self.label_precip.pack()

    def display_compare_list(self):
        self.reset_frame_by_name(self.frame_compare1)
        self.reset_frame_by_name(self.frame_compare2)

        self.listbox1 = Listbox(self.frame_compare1)
        self.listbox1.pack()

        self.listbox2 = Listbox(self.frame_compare2)
        self.listbox2.pack()

        self.stations_to_compare = []
        self.stations_closest = []

        for station in self.stations_can_compare:
            current_name = station.get("name")
            self.listbox1.insert(END, current_name)

        self.listbox1.bind("<<ListboxSelect>>", self.select_to_add)
        self.listbox2.bind("<<ListboxSelect>>", self.select_to_remove)

        self.button_add_compare_list = Button(self.frame_button_compare, text="Dodaj", command=self.add_to_compare_list, state=DISABLED)
        self.button_add_compare_list.pack(fill=BOTH)

        self.button_remove_compare_list = Button(self.frame_button_compare, text="Ukloni", command=self.remove_from_compare_list, state=DISABLED)
        self.button_remove_compare_list.pack(fill=BOTH)

        self.button_compare_selected = Button(self.frame_button_compare, text="Usporedi odabrane postaje", command=self.compare_selected_stations, state=DISABLED)
        self.button_compare_selected.pack(fill=BOTH)

        self.button_compare_closest = Button(self.frame_button_compare, text="Usporedi najbliže postaje", command=self.compare_closest_stations, state=DISABLED)
        self.button_compare_closest.pack(fill=BOTH)
        
        self.button_compare_detailed_7 = Button(self.frame_button_compare, text="Detaljna usporedba 7 dana", command=lambda: self.compare_2_stations(days=7), state=DISABLED)
        self.button_compare_detailed_7.pack(fill=BOTH)
        
        self.button_compare_detailed_31 = Button(self.frame_button_compare, text="Detaljna usporedba 1 mjesec", command=lambda: self.compare_2_stations(days=31), state=DISABLED)
        self.button_compare_detailed_31.pack(fill=BOTH)

    def reset_frame_by_name(self, frameName):
        for widget in frameName.winfo_children():
            widget.destroy()

    def select_to_add(self, e):
        self.button_remove_compare_list['state'] = DISABLED
        self.button_add_compare_list['state'] = DISABLED

        if len(self.stations_to_compare) >= self.max_number_of_stations_to_compare:
            return

        current_station_name = self.listbox1.get(ANCHOR)

        for station in self.stations_to_compare:
            if current_station_name in station.values():
                return
            
        for station in self.stations_dict_all:
            if current_station_name in station.values():
                self.selected_to_add = station
                self.button_add_compare_list['state'] = NORMAL
                break

    def select_to_remove(self, e):
        self.button_add_compare_list['state'] = DISABLED
        self.button_remove_compare_list['state'] = DISABLED

        current_station_name = self.listbox2.get(ANCHOR)

        for station in self.stations_to_compare:
            if current_station_name in station.values():
                self.selected_to_remove = station
                self.button_remove_compare_list['state'] = NORMAL
                break

    def add_to_compare_list(self):
        self.button_add_compare_list['state'] = DISABLED
        self.button_remove_compare_list['state'] = DISABLED

        self.stations_to_compare.append(self.selected_to_add)
        self.listbox2.insert(END, self.selected_to_add.get("name"))

        if len(self.stations_to_compare) > 0:
            self.button_compare_selected['state'] = NORMAL
        else:
            self.button_compare_selected['state'] = DISABLED
            
        if len(self.stations_to_compare) == 1:
            self.button_compare_detailed_7['state'] = NORMAL
            self.button_compare_detailed_31['state'] = NORMAL
        else:
            self.button_compare_detailed_7['state'] = DISABLED
            self.button_compare_detailed_31['state'] = DISABLED

    def remove_from_compare_list(self):
        self.button_add_compare_list['state'] = DISABLED
        self.button_remove_compare_list['state'] = DISABLED

        self.stations_to_compare.remove(self.selected_to_remove)
        self.listbox2.delete(ANCHOR)

        if len(self.stations_to_compare) > 0:
            self.button_compare_selected['state'] = NORMAL
        else:
            self.button_compare_selected['state'] = DISABLED
            
        if len(self.stations_to_compare) == 1:
            self.button_compare_detailed_7['state'] = NORMAL
            self.button_compare_detailed_31['state'] = NORMAL
        else:
            self.button_compare_detailed_7['state'] = DISABLED
            self.button_compare_detailed_31['state'] = DISABLED

    def compare_stations(self, stations_to_compare):
        json_files = []

        for station in stations_to_compare:
            json_file = station_data.get_station_json_file(station.get("url"))
            json_files.append(json_file)

        new_window = WindowCompareStations(json_files)
        
    def compare_stations_detailed(self, stations_to_compare, days):
        json_files = []
        
        for station in stations_to_compare:
            json_file = station_data.get_station_json_file(station.get("url"))
            json_files.append(json_file)

        new_window = WindowDetailedCompare(json_files, days)

    def compare_selected_stations(self):
        stations_to_compare = []
        stations_to_compare.append(self.station_info)
        stations_to_compare = stations_to_compare + self.stations_to_compare
        self.compare_stations(stations_to_compare)

    def compare_closest_stations(self):
        stations_to_compare = []
        stations_to_compare.append(self.station_info)
        stations_to_compare = stations_to_compare + self.stations_closest
        self.compare_stations(stations_to_compare)
        
    def compare_2_stations(self, days):
        stations_to_compare = []
        stations_to_compare.append(self.station_info)
        stations_to_compare = stations_to_compare + self.stations_to_compare
        self.compare_stations_detailed(stations_to_compare, days)

    def find_closest_stations(self):
        self.button_compare_closest['state'] = DISABLED
        station_coordinates = (self.lat, self.lon)
        
        stations_to_compare_to = []
        for station in self.stations_dict_all:
            if station.get("name") == self.name:
                continue
            current_station_json = station_data.get_station_json_file(station.get("url"))
            current_station = station_data.get_station_info_from_json(current_station_json)
            current_station_lat = current_station.get("lat")
            current_station_lon = current_station.get("lon")
            current_station_coordinates = (current_station_lat, current_station_lon)
            dist = distance.distance(station_coordinates, current_station_coordinates).km
            station["distance"] = dist
            stations_to_compare_to.append(station)
        
        stations_to_compare_to.sort(key=lambda x: x.get("distance"))
        stations_to_compare_to = stations_to_compare_to[:4]

        self.stations_closest = stations_to_compare_to

        if len(self.stations_closest) > 0:
            self.button_compare_closest['state'] = NORMAL
