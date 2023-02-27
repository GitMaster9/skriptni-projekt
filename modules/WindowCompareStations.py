from tkinter import *
import random
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

import modules.station_data as station_data

error_message = "Nema podataka"
offset_y = 0.03
random_limit = 100000

class WindowCompareStations:
    def __init__(self, stations_to_compare):
        self.stations_to_compare = stations_to_compare

        self.top = Toplevel()
        self.top.minsize(960, 720)
        self.top.title('Usporedba odabranih stanica')

        self.get_data_from_stations()

        self.graph_temps()
        self.graph_heats()
        self.graph_rhs()
        self.graph_presses()
        self.graph_wavgs()
        self.graph_precips()

        self.show_graphs()

    def get_data_from_stations(self):
        self.names = []
        self.temps = []
        self.heats = []
        self.rhs = []
        self.presses = []
        self.wavgs = []
        self.precips = []

        for station in self.stations_to_compare:
            current_station = station_data.get_station_info_from_json(station)
            name = current_station.get("name")
            temp = current_station.get("temp")
            heat = current_station.get("heat")
            rh = current_station.get("rh")
            press = current_station.get("press")
            wavg = current_station.get("wavg")
            precip = current_station.get("precip24")
            
            self.names.append(name)
            self.temps.append(temp)
            self.heats.append(heat)
            self.rhs.append(rh)
            self.presses.append(press)
            self.wavgs.append(wavg)
            self.precips.append(precip)

    def reset_frame_by_name(self, frameName):
        for widget in frameName.winfo_children():
            widget.destroy()

    def graph_temps(self):
        random_number = random.randint(0, random_limit)
        random_name = "Figure " + str(random_number)
        self.figure1 = plt.figure(random_name)

        for i in range(len(self.names)):
            plt.bar(self.names[i], self.temps[i], width=0.3, label=self.names[i])
            plt.text(i, self.temps[i] / 2, self.temps[i], ha = 'center')

        plt.title("Temperatura")
        plt.ylabel("°C")
        plt.legend()
        plt.savefig("temps.png")

    def graph_heats(self):
        random_number = random.randint(0, random_limit)
        random_name = "Figure " + str(random_number)
        self.figure2 = plt.figure(random_name)

        for i in range(len(self.names)):
            plt.bar(self.names[i], self.heats[i], width=0.3, label=self.names[i])
            plt.text(i, self.heats[i] / 2, self.heats[i], ha = 'center')

        plt.title("Osjećaj temperature")
        plt.ylabel("°C")
        plt.legend()
        plt.savefig("heats.png")

    def graph_rhs(self):
        random_number = random.randint(0, random_limit)
        random_name = "Figure " + str(random_number)
        self.figure3 = plt.figure(random_name)

        for i in range(len(self.names)):
            plt.bar(self.names[i], self.rhs[i], width=0.3, label=self.names[i])
            plt.text(i, self.rhs[i] / 2, self.rhs[i], ha = 'center')

        plt.title("Relativna vlažnost")
        plt.ylabel("%")
        plt.legend()
        plt.savefig("rhs.png")

    def graph_presses(self):
        random_number = random.randint(0, random_limit)
        random_name = "Figure " + str(random_number)
        self.figure4 = plt.figure(random_name)

        for i in range(len(self.names)):
            plt.bar(self.names[i], self.presses[i], width=0.3, label=self.names[i])
            plt.text(i, self.presses[i] / 2, self.presses[i], ha = 'center')

        plt.title("Tlak zraka")
        plt.ylabel("hPa")
        plt.legend()
        plt.savefig("presses.png")

    def graph_wavgs(self):
        random_number = random.randint(0, random_limit)
        random_name = "Figure " + str(random_number)
        self.figure5 = plt.figure(random_name)

        for i in range(len(self.names)):
            plt.bar(self.names[i], self.wavgs[i], width=0.3, label=self.names[i])
            plt.text(i, self.wavgs[i] / 2, self.wavgs[i], ha = 'center')

        plt.title("Brzina vjetra")
        plt.ylabel("m/s")
        plt.legend()
        plt.savefig("wavgs.png")

    def graph_precips(self):
        random_number = random.randint(0, random_limit)
        random_name = "Figure " + str(random_number)
        self.figure6 = plt.figure(random_name)

        for i in range(len(self.names)):
            plt.bar(self.names[i], self.precips[i], width=0.3, label=self.names[i])
            plt.text(i, self.precips[i] / 2, self.precips[i], ha = 'center')

        plt.title("Oborine u 24h")
        plt.ylabel("mm")
        plt.legend()
        plt.savefig("precips.png")

    def show_graphs(self):
        image_temps = Image.open("temps.png")
        image_tk_temps = ImageTk.PhotoImage(image_temps)

        image_heats = Image.open("heats.png")
        image_tk_heats = ImageTk.PhotoImage(image_heats)

        image_rhs = Image.open("rhs.png")
        image_tk_rhs = ImageTk.PhotoImage(image_rhs)

        image_presses = Image.open("presses.png")
        image_tk_presses = ImageTk.PhotoImage(image_presses)

        image_wavgs = Image.open("wavgs.png")
        image_tk_wavgs = ImageTk.PhotoImage(image_wavgs)

        image_precips = Image.open("precips.png")
        image_tk_precips = ImageTk.PhotoImage(image_precips)

        image_label_temps = Label(self.top, image=image_tk_temps)
        image_label_temps.grid(column=0, row=0)
        image_label_temps.image = image_tk_temps

        image_label_heats = Label(self.top, image=image_tk_heats)
        image_label_heats.grid(column=1, row=0)
        image_label_heats.image = image_tk_heats

        image_label_rhs = Label(self.top, image=image_tk_rhs)
        image_label_rhs.grid(column=2, row=0)
        image_label_rhs.image = image_tk_rhs

        image_label_presses = Label(self.top, image=image_tk_presses)
        image_label_presses.grid(column=0, row=1)
        image_label_presses.image = image_tk_presses

        image_label_wavgs = Label(self.top, image=image_tk_wavgs)
        image_label_wavgs.grid(column=1, row=1)
        image_label_wavgs.image = image_tk_wavgs

        image_label_precips = Label(self.top, image=image_tk_precips)
        image_label_precips.grid(column=2, row=1)
        image_label_precips.image = image_tk_precips
