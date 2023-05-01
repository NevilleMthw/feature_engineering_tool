import tkinter as tk

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