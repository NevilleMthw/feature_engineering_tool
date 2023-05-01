import tkinter as tk

class FeatureSelection:
    """A class that creates a UI for selecting a feature"""

    def __init__(self, master):
        """
        Initializes the FeatureSelection object.

        :param master: The parent widget.
        """
        self.master = master

        

        self.load_model_button = tk.Button(
            master, text="Load Model", command=self.load_model
        )
        self.load_model_button.pack()

        self.load_image_button = tk.Button(
            master, text="Load Image", command=self.load_image
        )
        self.load_image_button.pack()

        self.select_feature_button = tk.Button(
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