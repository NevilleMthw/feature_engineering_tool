import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt


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


class FeatureExtractWindow():
    """A class that creates a UI for loading and visualizing a feature"""

    def __init__(self, master):
        """
        Initializes the FeatureVisualization object.

        :param master: The parent widget.
        """

        self.master = master

        self.heading_Label = tk.Label(
            master, text="Feature Extraction Section", font=("Arial", 30)
        )
        self.heading_Label.pack(pady=20)

        self.heading_Label = tk.Label(
            master, text="Please choose from the following models, through which the features will be extracted.", font=("Arial", 20)
        )
        self.heading_Label.pack(pady=20)

        self.load_mobilenet_model = tk.Button(
            master, text="MobileNet-V2", command=self.mobilenetv2_model
        )
        self.load_mobilenet_model.pack(pady=10)

        self.load_vgg_model = tk.Button(
            master, text="VGG-16", command=self.vgg16_model
        )
        self.load_vgg_model.pack(pady=10)

        # self.load_resnet_model = tk.Button(
        #     master, text="ResNet-50", command=self.resnet50_model
        # )
        # self.load_resnet_model.pack()

        self.load_inception_model = tk.Button(
            master, text="Inception-V3", command=self.inceptionv3_model
        )
        self.load_inception_model.pack(pady=10)

        self.note_label = tk.Label(
            master, text="Note: Only one model must be chosen.", font=("Arial", 15, "bold")
        )
        self.note_label.pack(pady=20)

        self.model_imported_label = tk.Label(
            master, text="Model imported, saved to memory. Proceed to next tab.", font=("Arial", 12)
        )
        self.model_imported_label.pack(pady=10)


        # self.visualize_feature_button = tk.Button(
        #     master,
        #     text="Visualize Feature",
        #     command=self.visualize_feature,
        #     state="disabled",
        # )
        # self.visualize_feature_button.pack()

        self.canvas = tk.Canvas(master, width=100, height=100)
        self.canvas.pack()

    def mobilenetv2_model(self):
        """Loads the MobileNet-V2 model"""

        pass

    def vgg16_model(self):
        """Loads the VGG-16 model"""

        pass

    def resnet50_model(self):
        """Loads the ResNet-50 model"""

        pass

    def inceptionv3_model(self):
        """Loads the Inception-V3 model"""

        pass

class FeatureSelection:
    """A class that creates a UI for selecting a feature"""

    def __init__(self, master):
        """
        Initializes the FeatureSelection object.

        :param master: The parent widget.
        """
        self.master = master

        

        self.load_model_button = ttk.Button(
            master, text="Load Model", command=self.load_model
        )
        self.load_model_button.pack()

        self.load_image_button = ttk.Button(
            master, text="Load Image", command=self.load_image
        )
        self.load_image_button.pack()

        self.select_feature_button = ttk.Button(
            master, text="Select Feature", command=self.select_feature, state="disabled"
        )
        self.select_feature_button.pack()

        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()

    def load_model(self):
        """
        Loads a model
        """
        pass

    def load_image(self):
        """
        Loads an image
        """
        pass

    def select_feature(self):
        """
        Selects a feature
        """
        pass


class MainApplication:

    def __init__(self, master):
        """
        Initializes a new instance of the MainApplication class.

        Parameters
        ----------
        master : object
            The root window of the application.

        """
        self.master = master

        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill="both", expand=True)

        self.data_tab = tk.Frame(self.notebook)
        self.feature_extract_tab = tk.Frame(self.notebook)
        self.selection_tab = tk.Frame(self.notebook)

        self.notebook.add(self.data_tab, text="Dataset Import")
        self.notebook.add(self.feature_extract_tab, text="Feature Extraction")
        self.notebook.add(self.selection_tab, text="Feature Selection")

        self.data_import = DatasetImportWindow(self.data_tab)
        self.feature_ext = FeatureExtractWindow(self.feature_extract_tab)
        self.feature_sel = FeatureSelection(self.selection_tab)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Feature Engineering Tool")
    app = MainApplication(root)
    root.mainloop()
