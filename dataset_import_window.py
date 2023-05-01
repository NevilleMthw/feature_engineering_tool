import tkinter as tk

class DatasetImportWindow():
    """A class that creates a UI for loading and visualizing a model"""

    def __init__(self, master):
        """
        Initializes the ModelVisualization object.

        :param master: The parent widget.
        """

        self.master = master

        self.image_paths = []
        self.images = []

        self.heading_Label = tk.Label(
            master, text="Data Import Section", font=("Arial", 30)
        )
        self.heading_Label.pack(pady=20)

        self.data_Import_Button = tk.Button(
            master, text="Dataset Import", command=self.load_data, width=15, height=2
        )
        self.data_Import_Button.pack(anchor="center", pady=50)

        self.data_Imported_Label = tk.Label(
            master,
            text="Data Imported, saved to memory. Proceed to next tab.",
            font=("Arial", 12),
        )
        self.data_Imported_Label.pack(pady=10)

        # self.visualize_model_button = ttk.Button(master, text="Visualize Model", command=self.visualize_model, state='disabled')
        # self.visualize_model_button.pack()

        self.canvas = tk.Canvas(master, width=700, height=500)
        self.canvas.pack()

    def load_data(self):
        """Enables the visualize_model_button"""

        self.data_Import_Button["state"] = "normal"

    # def get_model_graph(self):
    #     """Generates a random 3D graph"""

    #     graph = np.random.rand(500, 500, 3)
    #     return graph