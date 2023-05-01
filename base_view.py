import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt


class DatasetImportWindow:
    """A class that creates a UI for loading and visualizing a model"""

    def __init__(self, master):
        """
        Initializes the ModelVisualization object.

        :param master: The parent widget.
        """

        self.master = master

        self.image_paths = []
        self.images = []

        self.heading_Label = tk.Label(master, text="Data Import Section", font=("Arial", 30))
        self.heading_Label.pack(pady=20)

        self.data_Import_Button = tk.Button(master, text="Dataset Import", command=self.load_data, width=15, height=2)
        self.data_Import_Button.pack(anchor='center', pady=50)

        self.data_Imported_Label = tk.Label(master, text="Data Imported, saved to memory. Proceed to next tab.", font=("Arial", 12))
        self.data_Imported_Label.pack(pady=10)

        # self.visualize_model_button = ttk.Button(master, text="Visualize Model", command=self.visualize_model, state='disabled')
        # self.visualize_model_button.pack()

        self.canvas = tk.Canvas(master, width=450, height=300)
        self.canvas.pack()

    def load_data(self):
        """Enables the visualize_model_button"""

        self.data_Import_Button['state'] = 'normal'

    # def get_model_graph(self):
    #     """Generates a random 3D graph"""

    #     graph = np.random.rand(500, 500, 3)
    #     return graph


class FeatureVisualization:
    """A class that creates a UI for loading and visualizing a feature"""

    def __init__(self, master):
        """
        Initializes the FeatureVisualization object.

        :param master: The parent widget.
        """

        self.master = master

        self.load_feature_button = ttk.Button(master, text="Load Feature", command=self.load_feature)
        self.load_feature_button.pack()

        self.visualize_feature_button = ttk.Button(master, text="Visualize Feature", command=self.visualize_feature, state='disabled')
        self.visualize_feature_button.pack()

        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()

    def load_feature(self):
        """Enables the visualize_feature_button"""

        self.visualize_feature_button['state'] = 'normal'

    def visualize_feature(self):
        """Visualizes a randomly generated feature using PIL and Tkinter"""

        feature = self.get_feature()
        img = Image.fromarray(np.uint8(feature))
        img_tk = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor='nw', image=img_tk)

    def get_feature(self):
        """Generates a random 3D feature"""

        feature = np.random.rand(500, 500, 3) * 255
        return feature


class FeatureSelection:
    """A class that creates a UI for selecting a feature"""

    def __init__(self, master):
        """
        Initializes the FeatureSelection object.

        :param master: The parent widget.
        """
        self.master = master

        self.load_model_button = ttk.Button(master, text="Load Model", command=self.load_model)
        self.load_model_button.pack()

        self.load_image_button = ttk.Button(master, text="Load Image", command=self.load_image)
        self.load_image_button.pack()

        self.select_feature_button = ttk.Button(master, text="Select Feature", command=self.select_feature, state='disabled')
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
    """
    A class that represents the main application of the feature engineering tool.

    Attributes
    ----------
    master : object
        The root window of the application.

    notebook : object
        The notebook widget that contains the tabs for model visualization, feature visualization, and feature selection.

    model_tab : object
        The tab that displays the model visualization interface.

    feature_tab : object
        The tab that displays the feature visualization interface.

    selection_tab : object
        The tab that displays the feature selection interface.

    model_viz : object
        An instance of the ModelVisualization class that represents the model visualization interface.

    feature_viz : object
        An instance of the FeatureVisualization class that represents the feature visualization interface.

    feature_sel : object
        An instance of the FeatureSelection class that represents the feature selection interface.

    Methods
    -------
    __init__(self, master)
        Initializes a new instance of the MainApplication class.

    """
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
        self.notebook.pack(fill='both', expand=True)

        self.data_tab = ttk.Frame(self.notebook)
        self.feature_tab = ttk.Frame(self.notebook)
        self.selection_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.data_tab, text='Dataset Import Window')
        self.notebook.add(self.feature_tab, text='Feature Visualization')
        self.notebook.add(self.selection_tab, text='Feature Selection')

        self.data_import = DatasetImportWindow(self.data_tab)
        self.feature_viz = FeatureVisualization(self.feature_tab)
        self.feature_sel = FeatureSelection(self.selection_tab)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Feature Engineering Tool")
    app = MainApplication(root)
    root.mainloop()


