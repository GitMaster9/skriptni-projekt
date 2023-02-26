from tkinter import *
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import ttk

error_message = "Nema podataka"
offset_y = 0.03

class WindowCompareStations:
    def __init__(self, json_file, stations_to_compare):
        self.json_file = json_file
        self.stations_to_compare = stations_to_compare

        self.top = Toplevel()
        self.top.minsize(960, 720) # 1280, 720 # 800, 600
        self.top.title('Usporedba stanica')

        self.get_data_from_stations()

        self.graph_temps()
        self.graph_heats()
        self.graph_rhs()
        self.graph_presses()
        self.graph_wavgs()

        self.show_graphs()

    def get_data_from_stations(self):
        self.names = []
        name = self.json_file.get("data").get("station").get("name")
        self.names.append(name)

        self.temps = []
        temp = self.json_file.get("data").get("last").get("temp")
        self.temps.append(temp)

        self.heats = []
        heat = self.json_file.get("data").get("last").get("heat")
        self.heats.append(heat)

        self.rhs = []
        rh = self.json_file.get("data").get("last").get("rh")
        self.rhs.append(rh)

        self.presses = []
        press = self.json_file.get("data").get("last").get("press")
        self.presses.append(press)

        self.wavgs = []
        wavg = self.json_file.get("data").get("last").get("wavg")
        self.wavgs.append(wavg)

        for station in self.stations_to_compare:
            name = station.get("data").get("station").get("name")
            temp = station.get("data").get("last").get("temp")
            heat = station.get("data").get("last").get("heat")
            rh = station.get("data").get("last").get("rh")
            press = station.get("data").get("last").get("press")
            wavg = station.get("data").get("last").get("wavg")
            self.names.append(name)
            self.temps.append(temp)
            self.heats.append(heat)
            self.rhs.append(rh)
            self.presses.append(press)
            self.wavgs.append(wavg)

    def reset_frame_by_name(self, frameName):
        for widget in frameName.winfo_children():
            widget.destroy()

    def graph_temps(self):
        self.figure1 = plt.figure("Figure 1")

        plt.bar(self.names, self.temps, width=0.3)

        for i in range(len(self.names)):
            plt.text(i, self.temps[i] / 2, self.temps[i], ha = 'center')

        plt.title("Temperature")
        plt.ylabel("Stupnjevi C")
        plt.savefig("temps.png")

    def graph_heats(self):
        self.figure1 = plt.figure("Figure 2")

        plt.bar(self.names, self.heats, width=0.3)

        for i in range(len(self.names)):
            plt.text(i, self.heats[i] / 2, self.heats[i], ha = 'center')

        plt.title("Osjećaj temperature")
        plt.ylabel("Stupnjevi C")
        plt.savefig("heats.png")

    def graph_rhs(self):
        self.figure2 = plt.figure("Figure 3")

        plt.bar(self.names, self.rhs, width=0.3)

        for i in range(len(self.names)):
            plt.text(i, self.rhs[i] / 2, self.rhs[i], ha = 'center')

        plt.title("Relativna vlažnost")
        plt.ylabel("Postotak %")
        plt.savefig("rhs.png")

    def graph_presses(self):
        self.figure1 = plt.figure("Figure 4")

        plt.bar(self.names, self.presses, width=0.3)

        for i in range(len(self.names)):
            plt.text(i, self.presses[i] / 2, self.presses[i], ha = 'center')

        plt.title("Tlak zraka")
        plt.ylabel("pritisak hPa")
        plt.savefig("presses.png")

    def graph_wavgs(self):
        self.figure1 = plt.figure("Figure 5")

        plt.bar(self.names, self.wavgs, width=0.3)

        for i in range(len(self.names)):
            plt.text(i, self.wavgs[i] / 2, self.wavgs[i], ha = 'center')

        plt.title("Brzina vjetra")
        plt.ylabel("brzina m/s")
        plt.savefig("wavgs.png")

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
