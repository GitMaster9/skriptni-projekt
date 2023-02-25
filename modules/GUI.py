from tkinter import *
from tkinter import ttk

error_message = "Nema podataka"

class ButtonStation:
    def __init__(self, master, text_to_display, url_to_send, function_to_start):
        self.master = master
        self.text_to_display = text_to_display
        self.url_to_send = url_to_send

        self.button_to_display = Button(self.master, text=self.text_to_display, command=lambda: function_to_start(self.url_to_send))
        self.button_to_display.pack(fill=BOTH)

class WindowStationInfo:
    def __init__(self, json_file, stations_dict_all):
        self.json_file = json_file
        self.stations_dict_all = stations_dict_all

        self.top = Toplevel()
        self.top.minsize(960, 720) # 1280, 720 # 800, 600
        self.top.title('Stanica')

        self.frame_name = LabelFrame(self.top)
        self.frame_stats_datetime = LabelFrame(self.top)
        self.frame_stats_placeholder = LabelFrame(self.top)
        self.frame_stats = LabelFrame(self.top)
        self.frame_compare1 = LabelFrame(self.top)
        self.frame_compare2 = LabelFrame(self.top)
        self.frame_button_compare = LabelFrame(self.top)

        self.frame_name.place(relx=0.5, rely=0.1, anchor=N)
        self.frame_stats_datetime.place(relx=0.5, rely=0.2, anchor=N)
        self.frame_stats_placeholder.place(relx=0.45, rely=0.3, anchor=N)
        self.frame_stats.place(relx=0.55, rely=0.3, anchor=N)
        self.frame_compare1.place(relx=0.4, rely=0.6, anchor=N)
        self.frame_compare2.place(relx=0.6, rely=0.6, anchor=N)
        self.frame_button_compare.place(relx=0.5, rely=0.9, anchor=N)

        self.get_all_station_data(self.json_file)
        self.display_station_info_placeholder()
        self.display_station_info()
        self.display_compare_list()

        self.top.mainloop()

    def get_all_station_data(self, json_file):
        self.datetime = json_file.get("data").get("last").get("datetime")
        if (self.datetime == None):
            self.datetime = error_message

        self.name = json_file.get("data").get("station").get("name")
        if (self.name == None):
            self.name = error_message

        self.temp = json_file.get("data").get("last").get("temp")
        if (self.temp == None):
            self.temp = error_message
        else:
            self.temp = str(self.temp) + " °C"

        self.heat = json_file.get("data").get("last").get("heat")
        if (self.heat == None):
            self.heat = error_message
        else:
            self.heat = str(self.heat) + " °C"

        self.rh = json_file.get("data").get("last").get("rh")
        if (self.rh == None):
            self.rh = error_message
        else:
            self.rh = str(self.rh) + "%"

        self.press = json_file.get("data").get("last").get("press")
        if (self.press == None):
            self.press = error_message
        else:
            self.press = str(self.press) + " hPa"

        self.wavg = json_file.get("data").get("last").get("wavg")
        if (self.wavg == None):
            self.wavg = error_message
        else:
            self.wavg = str(self.wavg) + " m/s"

        self.stations_all = []

        for station in self.stations_dict_all:
            current_name = station.get("name")
            if (current_name != self.name):
                self.stations_all.append(current_name)

    def display_station_info_placeholder(self):
        self.reset_frame_by_name(self.frame_stats_placeholder)

        text1 = "Temperatura: "
        text2 = "Osjet temperature: "
        text3 = "Relativna vlažnost: "
        text4 = "Tlak zraka: "
        text5 = "Brzina vjetra : "

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

    def display_compare_list(self):
        self.reset_frame_by_name(self.frame_compare1)
        self.reset_frame_by_name(self.frame_compare2)

        self.listbox1 = Listbox(self.frame_compare1)
        self.listbox1.pack()

        self.listbox2 = Listbox(self.frame_compare2)
        self.listbox2.pack()

        self.stations_to_compare = []

        for station in self.stations_all:
            self.listbox1.insert(END, station)

        self.listbox1.bind("<<ListboxSelect>>", self.select_to_add)
        self.listbox2.bind("<<ListboxSelect>>", self.select_to_remove)

        self.button_add_compare_list = Button(self.frame_button_compare, text="Add", command=self.add_to_compare_list, state=DISABLED)
        self.button_add_compare_list.pack(fill=BOTH)

        self.button_remove_compare_list = Button(self.frame_button_compare, text="Remove", command=self.remove_from_compare_list, state=DISABLED)
        self.button_remove_compare_list.pack(fill=BOTH)

        self.button_compare = Button(self.frame_button_compare, text="Compare", command=self.compare_list, state=DISABLED)
        self.button_compare.pack(fill=BOTH)

    def reset_frame_by_name(self, frameName):
        for widget in frameName.winfo_children():
            widget.destroy()

    def select_to_add(self, e):
        self.button_remove_compare_list['state'] = DISABLED
        self.button_add_compare_list['state'] = DISABLED

        self.selected_to_add = self.listbox1.get(ANCHOR)

        result = self.stations_to_compare.count(self.selected_to_add)

        if result == 0:
            self.button_add_compare_list['state'] = NORMAL

    def select_to_remove(self, e):
        self.button_add_compare_list['state'] = DISABLED
        self.button_remove_compare_list['state'] = DISABLED

        self.selected_to_remove = self.listbox2.get(ANCHOR)

        self.button_remove_compare_list['state'] = NORMAL

    def add_to_compare_list(self):
        self.button_add_compare_list['state'] = DISABLED
        self.button_remove_compare_list['state'] = DISABLED

        self.stations_to_compare.append(self.selected_to_add)
        self.listbox2.insert(END, self.selected_to_add)

        if len(self.stations_to_compare) > 0:
            self.button_compare['state'] = NORMAL
        else:
            self.button_compare['state'] = DISABLED

    def remove_from_compare_list(self):
        self.button_add_compare_list['state'] = DISABLED
        self.button_remove_compare_list['state'] = DISABLED

        self.stations_to_compare.remove(self.selected_to_remove)
        self.listbox2.delete(ANCHOR)

        if len(self.stations_to_compare) > 0:
            self.button_compare['state'] = NORMAL
        else:
            self.button_compare['state'] = DISABLED

    def compare_list(self):
        print("COMPARE")

# heat - osjet temperature
# wgust - udari vjetra
# wavg - brzina vjetra
# wdir - smjer vjetra