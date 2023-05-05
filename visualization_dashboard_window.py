import tkinter as tk

class VisualizationDashboard:
    """A class that creates a visualization dashboard"""

    def __init__(self, master):
        """
        Initializes the VisualizationDashboard object.

        :param master: The parent widget.
        """
        self.master = master

        self.frame1 = tk.Frame(master, width=400, height=400, bg="white")
        self.frame1.grid(row=0, column=0)

        self.frame2 = tk.Frame(master, width=400, height=400, bg="grey")
        self.frame2.grid(row=0, column=1)

        self.frame3 = tk.Frame(master, width=400, height=400, bg="black")
        self.frame3.grid(row=1, column=0)

        self.frame4 = tk.Frame(master, width=400, height=400, bg="red")
        self.frame4.grid(row=1, column=1)
