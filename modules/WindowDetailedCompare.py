from tkinter import *
from tkinter import ttk
import random
import numpy as np

import matplotlib.pyplot as plt
from PIL import Image, ImageTk

from datetime import datetime

from modules.ScrollableFrame import ScrollableFrame

error_message = "Nema podataka"
offset_y = 0.03
random_limit = 100000

class WindowDetailedCompare:
    def __init__(self, json_files, days):
        self.json_files = json_files

        self.top = Toplevel()
        self.top.minsize(1600, 800)
        self.top.title('Usporedba odabranih stanica')

        self.get_data_from_stations()

        self.graph_temps_x_days(days)
        self.graph_rhs_x_days(days)
        self.graph_presses_x_days(days)
        self.graph_wavgs_x_days(days)
        self.graph_wdirs_x_days(days)
        self.graph_precips_x_days(days)

        self.show_graphs(days)

    def get_data_from_stations(self):
        self.names = []
        name1 = self.json_files[0].get("data").get("station").get("name")
        self.names.append(name1)
        name2 = self.json_files[1].get("data").get("station").get("name")
        self.names.append(name2)
        
        station_1_data = self.json_files[0].get("data").get("archive").get("daily")
        station_2_data = self.json_files[1].get("data").get("archive").get("daily")
        
        # datetime
        self.datetimes = []
        datetimes1 = station_1_data.get("datetime")
        self.datetimes.append(datetimes1)
        datetimes2 = station_2_data.get("datetime")
        self.datetimes.append(datetimes2)

        # temperature
        self.tempsL = []
        tempsL1 = station_1_data.get("tempL")
        self.tempsL.append(tempsL1)
        tempsL2 = station_2_data.get("tempL")
        self.tempsL.append(tempsL2)
        
        self.tempsH = []
        tempsH1 = station_1_data.get("tempH")
        self.tempsH.append(tempsH1)
        tempsH2 = station_2_data.get("tempH")
        self.tempsH.append(tempsH2)
        
        self.tempsA = []
        tempsA1 = station_1_data.get("tempA")
        self.tempsA.append(tempsA1)
        tempsA2 = station_2_data.get("tempA")
        self.tempsA.append(tempsA2)
        
        # relative humidity
        self.rhsL = []
        rhsL1 = station_1_data.get("rhL")
        self.rhsL.append(rhsL1)
        rhsL2 = station_2_data.get("rhL")
        self.rhsL.append(rhsL2)
        
        self.rhsH = []
        rhsH1 = station_1_data.get("rhH")
        self.rhsH.append(rhsH1)
        rhsH2 = station_2_data.get("rhH")
        self.rhsH.append(rhsH2)
        
        self.rhsA = []
        rhsA1 = station_1_data.get("rhA")
        self.rhsA.append(rhsA1)
        rhsA2 = station_2_data.get("rhA")
        self.rhsA.append(rhsA2)
        
        # pressure
        self.pressesL = []
        pressL1 = station_1_data.get("pressL")
        self.pressesL.append(pressL1)
        pressL2 = station_2_data.get("pressL")
        self.pressesL.append(pressL2)
        
        self.pressesH = []
        pressH1 = station_1_data.get("pressH")
        self.pressesH.append(pressH1)
        pressH2 = station_2_data.get("pressH")
        self.pressesH.append(pressH2)
        
        self.pressesA = []
        pressA1 = station_1_data.get("pressA")
        self.pressesA.append(pressA1)
        pressA2 = station_2_data.get("pressA")
        self.pressesA.append(pressA2)
        
        # wind
        self.wavgsA = []
        wavgsA1 = station_1_data.get("wavgA")
        self.wavgsA.append(wavgsA1)
        wavgsA2 = station_2_data.get("wavgA")
        self.wavgsA.append(wavgsA2)
        
        self.wgustsH = []
        wgustH1 = station_1_data.get("wgustH")
        self.wgustsH.append(wgustH1)
        wgustH2 = station_2_data.get("wgustH")
        self.wgustsH.append(wgustH2)
        
        self.wdirsA = []
        wdirsA1 = station_1_data.get("wdirA") if station_1_data.get("wdirA") else None
        self.wdirsA.append(wdirsA1)
        wdirsA2 = station_2_data.get("wdirA") if station_2_data.get("wdirA") else None
        self.wdirsA.append(wdirsA2)
      
        # precipitation        
        self.precips = []
        precips1 = station_1_data.get("precip") if station_1_data.get("precip") else None
        self.precips.append(precips1)
        precips2 = station_2_data.get("precip") if station_2_data.get("precip") else None
        self.precips.append(precips2)

    def reset_frame_by_name(self, frameName):
        for widget in frameName.winfo_children():
            widget.destroy()
            
    # function to create line graph for temperature in the last 7 days for 2 stations
    def graph_temps_x_days(self, days):
        random_number = random.randint(0, random_limit)
        random_name = "Figure " + str(random_number)
        self.figure1 = plt.figure(random_name, figsize=(16, 4))
        
        dates = [np.array([datetime.utcfromtimestamp(date).strftime("%d/%m/%Y") for date in self.datetimes[0][-days:]]),
                 np.array([datetime.utcfromtimestamp(date).strftime("%d/%m/%Y") for date in self.datetimes[1][-days:]])]
        temps1 = np.array(self.tempsA[0][-days:])
        temps2 = np.array(self.tempsA[1][-days:])
        temps = [temps1, temps2]

        for i in range(len(self.names)):
            plt.plot(dates[i],
                     temps[i],
                     marker="o",
                     label=self.names[i])
        
        plt.fill_between(dates[0],
                         temps1,
                         temps2,
                         where=(temps1 > temps2),
                         color="red",
                         alpha=0.2,
                         interpolate=True)
        plt.fill_between(dates[0],
                         temps1,
                         temps2,
                         where=(temps1 < temps2),
                         color="blue",
                         alpha=0.2,
                         interpolate=True)

        plt.title("Temperatura u posljednjih 7 dana")
        plt.ylabel("°C", rotation=0, fontsize=15, labelpad=15)
        ticks = dates[0][::3 if days == 31 else 1]
        plt.xticks(ticks)
        plt.grid(linestyle="--")
        plt.legend()
        plt.savefig(f"temps_{days}_days.png")
        
    # function to create line graph for relative humidity (rhsA) in the last 7 days for 2 stations
    def graph_rhs_x_days(self, days):
        random_number = random.randint(0, random_limit)
        random_name = "Figure " + str(random_number)
        self.figure2 = plt.figure(random_name, figsize=(16, 4))
        
        dates = [np.array([datetime.utcfromtimestamp(date).strftime("%d/%m/%Y") for date in self.datetimes[0][-days:]]),
                 np.array([datetime.utcfromtimestamp(date).strftime("%d/%m/%Y") for date in self.datetimes[1][-days:]])]
        rhs1 = np.array(self.rhsA[0][-days:])
        rhs2 = np.array(self.rhsA[1][-days:])
        rhs = [rhs1, rhs2]

        for i in range(len(self.names)):
            plt.plot(dates[i],
                     rhs[i],
                     marker="o",
                     label=self.names[i])
        
        plt.fill_between(dates[0],
                         rhs1,
                         rhs2,
                         where=(rhs1 > rhs2),
                         color="red",
                         alpha=0.2,
                         interpolate=True)
        plt.fill_between(dates[0],
                         rhs1,
                         rhs2,
                         where=(rhs1 < rhs2),
                         color="blue",
                         alpha=0.2,
                         interpolate=True)

        plt.title("Relativna vlažnost u posljednjih 7 dana")
        plt.ylabel("%", rotation=0, fontsize=15, labelpad=15)
        ticks = dates[0][::3 if days == 31 else 1]
        plt.xticks(ticks)
        plt.grid(linestyle="--")
        plt.legend()
        plt.savefig(f"rhs_{days}_days.png")
        
    # function to create line graph for pressure (pressesA) in the last 7 days for 2 stations
    def graph_presses_x_days(self, days):
        random_number = random.randint(0, random_limit)
        random_name = "Figure " + str(random_number)
        self.figure3 = plt.figure(random_name, figsize=(16, 4))
        
        dates = [np.array([datetime.utcfromtimestamp(date).strftime("%d/%m/%Y") for date in self.datetimes[0][-days:]]),
                 np.array([datetime.utcfromtimestamp(date).strftime("%d/%m/%Y") for date in self.datetimes[1][-days:]])]
        press1 = np.array(self.pressesA[0][-days:])
        press2 = np.array(self.pressesA[1][-days:])
        press = [press1, press2]

        for i in range(len(self.names)):
            plt.plot(dates[i],
                     press[i],
                     marker="o",
                     label=self.names[i])
        
        plt.fill_between(dates[0],
                         press1,
                         press2,
                         where=(press1 > press2),
                         color="red",
                         alpha=0.2,
                         interpolate=True)
        plt.fill_between(dates[0],
                         press1,
                         press2,
                         where=(press1 < press2),
                         color="blue",
                         alpha=0.2,
                         interpolate=True)

        plt.title("Tlak zraka u posljednjih 7 dana")
        plt.ylabel("hPa", rotation=0, fontsize=15, labelpad=15)
        ticks = dates[0][::3 if days == 31 else 1]
        plt.xticks(ticks)
        plt.grid(linestyle="--")
        plt.legend()
        plt.savefig(f"presses_{days}_days.png")
        
    # function to create line graph for wind speed (wavgsA) in the last 7 days for 2 stations
    def graph_wavgs_x_days(self, days):
        random_number = random.randint(0, random_limit)
        random_name = "Figure " + str(random_number)
        self.figure4 = plt.figure(random_name, figsize=(16, 4))
        
        dates = [np.array([datetime.utcfromtimestamp(date).strftime("%d/%m/%Y") for date in self.datetimes[0][-days:]]),
                 np.array([datetime.utcfromtimestamp(date).strftime("%d/%m/%Y") for date in self.datetimes[1][-days:]])]
        wavgs1 = np.array(self.wavgsA[0][-days:])
        wavgs2 = np.array(self.wavgsA[1][-days:])
        wavgs = [wavgs1, wavgs2]

        for i in range(len(self.names)):
            plt.plot(dates[i],
                     wavgs[i],
                     marker="o",
                     label=self.names[i])
        
        plt.fill_between(dates[0],
                         wavgs1,
                         wavgs2,
                         where=(wavgs1 > wavgs2),
                         color="red",
                         alpha=0.2,
                         interpolate=True)
        plt.fill_between(dates[0],
                         wavgs1,
                         wavgs2,
                         where=(wavgs1 < wavgs2),
                         color="blue",
                         alpha=0.2,
                         interpolate=True)

        plt.title("Brzina vjetra u posljednjih 7 dana")
        plt.ylabel("m/s", rotation=0, fontsize=15, labelpad=15)
        ticks = dates[0][::3 if days == 31 else 1]
        plt.xticks(ticks)
        plt.grid(linestyle="--")
        plt.legend()
        plt.savefig(f"wavgs_{days}_days.png")
        
    # function to create scatter graph for wind direction (wdirsA) in the last 7 days for 2 stations,
    # wind direction is in degrees,
    # y axis is labeled with cardinal directions
    def graph_wdirs_x_days(self, days):
        random_number = random.randint(0, random_limit)
        random_name = "Figure " + str(random_number)
        self.figure5 = plt.figure(random_name, figsize=(16, 4))
        
        dates = [np.array([datetime.utcfromtimestamp(date).strftime("%d/%m/%Y") for date in self.datetimes[0][-days:]]),
                 np.array([datetime.utcfromtimestamp(date).strftime("%d/%m/%Y") for date in self.datetimes[1][-days:]])]
        wdirs1 = np.array(self.wdirsA[0][-days:]) if self.wdirsA[0] else np.full(days, 0)
        wdirs2 = np.array(self.wdirsA[1][-days:]) if self.wdirsA[1] else np.full(days, 0)
        wdirs = [wdirs1, wdirs2]

        for i in range(len(self.names)):
            plt.scatter(dates[i],
                     wdirs[i],
                     marker="o",
                     label=self.names[i])

        plt.title("Smjer vjetra u posljednjih 7 dana")
        plt.ylabel("Smjer", rotation=0, fontsize=15, labelpad=25)
        plt.yticks([0, 22.5, 45, 67.5, 90, 112.5, 135, 157.5, 180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5, 360],
                   ["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW", "N"])
        ticks = dates[0][::3 if days == 31 else 1]
        plt.xticks(ticks)
        plt.grid(linestyle="--")
        plt.legend()
        plt.savefig(f"wdirs_{days}_days.png")

        
    # function to create line graph for wind precipitation (precips) in the last 7 days for 2 stations
    def graph_precips_x_days(self, days):
        random_number = random.randint(0, random_limit)
        random_name = "Figure " + str(random_number)
        self.figure5 = plt.figure(random_name, figsize=(16, 4))
        
        dates = [np.array([datetime.utcfromtimestamp(date).strftime("%d/%m/%Y") for date in self.datetimes[0][-days:]]),
                 np.array([datetime.utcfromtimestamp(date).strftime("%d/%m/%Y") for date in self.datetimes[1][-days:]])]
        precips1 = np.array(self.precips[0][-days:]) if self.precips[0] else np.full(days, 0)
        precips2 = np.array(self.precips[1][-days:]) if self.precips[1] else np.full(days, 0)
        precips = [precips1, precips2]

        for i in range(len(self.names)):
            plt.plot(dates[i],
                     precips[i],
                     marker="o",
                     label=self.names[i])
        
        plt.fill_between(dates[0],
                         precips1,
                         precips2,
                         where=(precips1 > precips2),
                         color="red",
                         alpha=0.2,
                         interpolate=True)
        plt.fill_between(dates[0],
                         precips1,
                         precips2,
                         where=(precips1 < precips2),
                         color="blue",
                         alpha=0.2,
                         interpolate=True)

        plt.title("Oborine u posljednjih 7 dana")
        plt.ylabel("mm", rotation=0, fontsize=15, labelpad=15)
        ticks = dates[0][::3 if days == 31 else 1]
        plt.xticks(ticks)
        plt.grid(linestyle="--")
        plt.legend()
        plt.savefig(f"precips_{days}_days.png")

    def show_graphs(self, days):
        scrollable_frame = ScrollableFrame(self.top)
      
        image_temps_x_days = Image.open(f"temps_{days}_days.png")
        image_tk_temps = ImageTk.PhotoImage(image_temps_x_days)
        
        image_rhs_x_days = Image.open(f"rhs_{days}_days.png")
        image_tk_rhs = ImageTk.PhotoImage(image_rhs_x_days)
        
        image_presses_x_days = Image.open(f"presses_{days}_days.png")
        image_tk_presses = ImageTk.PhotoImage(image_presses_x_days)
        
        image_wavgs_x_days = Image.open(f"wavgs_{days}_days.png")
        image_tk_wavgs = ImageTk.PhotoImage(image_wavgs_x_days)
        
        image_wdirs_x_days = Image.open(f"wdirs_{days}_days.png")
        image_tk_wdirs = ImageTk.PhotoImage(image_wdirs_x_days)
        
        image_precips_x_days = Image.open(f"precips_{days}_days.png")
        image_tk_precips = ImageTk.PhotoImage(image_precips_x_days)

        image_label_temps = Label(scrollable_frame.scrollable_frame, image=image_tk_temps)
        image_label_temps.grid(row=0)
        image_label_temps.image = image_tk_temps
        
        image_label_rhs = Label(scrollable_frame.scrollable_frame, image=image_tk_rhs)
        image_label_rhs.grid(row=1)
        image_label_rhs.image = image_tk_rhs
        
        image_label_presses = Label(scrollable_frame.scrollable_frame, image=image_tk_presses)
        image_label_presses.grid(row=2)
        image_label_presses.image = image_tk_presses
        
        image_label_wavgs = Label(scrollable_frame.scrollable_frame, image=image_tk_wavgs)
        image_label_wavgs.grid(row=3)
        image_label_wavgs.image = image_tk_wavgs
        
        image_label_wdirs = Label(scrollable_frame.scrollable_frame, image=image_tk_wdirs)
        image_label_wdirs.grid(row=4)
        image_label_wdirs.image = image_tk_wdirs
        
        image_label_precips = Label(scrollable_frame.scrollable_frame, image=image_tk_precips)
        image_label_precips.grid(row=5)
        image_label_precips.image = image_tk_precips
        
        scrollable_frame.pack(side="left", fill="both", expand=True)
