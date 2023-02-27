import sys
import tkinter as tk
from tkinter import ttk


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        if sys.platform.startswith("darwin"):
            # enable mousewheel scrolling on mac
            canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(-1*(event.delta), "units"))
        elif sys.platform == "linux":
            # enable mousewheel scrolling on linux
            canvas.bind_all("<4>", lambda event: canvas.yview_scroll(-1, "units"))
            canvas.bind_all("<5>", lambda event: canvas.yview_scroll(1, "units"))
        else:
            # enable mousewheel scrolling on windows
            canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))
            

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
