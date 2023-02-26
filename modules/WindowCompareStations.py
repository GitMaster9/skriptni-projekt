from tkinter import *

error_message = "Nema podataka"

class WindowCompareStations:
    def __init__(self, json_file, stations_to_compare):
        self.json_file = json_file
        self.stations_to_compare = stations_to_compare

        self.top = Toplevel()
        self.top.minsize(960, 720) # 1280, 720 # 800, 600
        self.top.title('Usporedba stanica')

        self.frame_name = LabelFrame(self.top)
        self.frame_stations = LabelFrame(self.top)

        self.frame_name.place(relx=0.5, rely=0.1, anchor=N)
        self.frame_stations.place(relx=0.5, rely=0.4, anchor=N)

        self.display_comparison()

    def display_comparison(self):
        self.reset_frame_by_name(self.frame_name)
        self.reset_frame_by_name(self.frame_stations)

        #self.label_name = Label(self.frame_name, text=name)
        #self.label_name.pack()

        names = []
        name = self.json_file.get("data").get("station").get("name")
        if (name == None):
            name = error_message
        names.append(name)

        temps = []
        temp = self.json_file.get("data").get("last").get("temp")
        if (temp == None):
            temp = error_message
        temps.append(temp)

        heats = []
        heat = self.json_file.get("data").get("last").get("heat")
        if (heat == None):
            heat = error_message
        heats.append(heat)

        rhs = []
        rh = self.json_file.get("data").get("last").get("rh")
        if (rh == None):
            rh = error_message
        rhs.append(rh)

        presses = []
        press = self.json_file.get("data").get("last").get("press")
        if (press == None):
            press = error_message
        presses.append(press)

        wavgs = []
        wavg = self.json_file.get("data").get("last").get("wavg")
        if (wavg == None):
            wavg = error_message
        wavgs.append(wavg)

        for station in self.stations_to_compare:
            name = station.get("data").get("station").get("name")
            temp = station.get("data").get("last").get("temp")
            heat = station.get("data").get("last").get("heat")
            rh = station.get("data").get("last").get("rh")
            press = station.get("data").get("last").get("press")
            wavg = station.get("data").get("last").get("wavg")
            names.append(name)
            temps.append(temp)
            heats.append(heat)
            rhs.append(rh)
            presses.append(press)
            wavgs.append(wavg)

        # ------------------------------------------------

        print(names)
        print(temps)
        print(heats)
        print(rhs)
        print(presses)
        print(wavgs)

    def reset_frame_by_name(self, frameName):
        for widget in frameName.winfo_children():
            widget.destroy()