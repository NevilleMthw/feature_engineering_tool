import tkinter as tk
import torchvision.models as models
import torch
from dataset_import_window import DatasetImportWindow

class FeatureExtractWindow:
    """A class that creates a UI for loading and visualizing a feature"""

    def __init__(self, master, data: DatasetImportWindow):
        """
        Initializes the FeatureVisualization object.

        :param master: The parent widget.
        """
        self.inherited_data = data.get_dataloader
        self.master = master

        self.feature_heading_Label = tk.Label(
            master, text="Feature Extraction Section", font=("Arial", 30)
        )
        self.feature_heading_Label.pack(pady=5)

        self.feature_choice_label = tk.Label(
            master,
            text="Please choose from the following models, through which the features will be extracted.",
            font=("Arial", 20),
        )
        self.feature_choice_label.pack(pady=20)

        self.load_mobilenet_model = tk.Button(
            master, text="MobileNet-V2", command=self.mobilenetv2_model
        )
        self.load_mobilenet_model.pack(pady=10)

        self.load_vgg_model = tk.Button(master, text="VGG-16", command=self.vgg16_model)
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
            master,
            text="Note: Only one model must be chosen.",
            font=("Arial", 15, "bold"),
        )
        self.note_label.pack(pady=20)

        self.model_Imported_Label = tk.Label(
            master,
            text="",
            font=("Arial", 12),
        )
        self.model_Imported_Label.pack(pady=10)

        self.visualize_feature_button = tk.Button(
            master,
            text="Store Features",
            command=self.store_visualized_features
        )
        self.visualize_feature_button.pack()

        self.canvas = tk.Canvas(master, width=100, height=100)
        self.canvas.pack()

    def mobilenetv2_model(self):
        """Loads the MobileNet-V2 model"""

        self.model = models.mobilenet_v3_small(pretrained=True, weights="IMAGENET1K_V1")

        self.model.eval()

        print("MobileNetV3 model loaded successfully.")

        self.model_Imported_Label.config(text="MobileNetV3 model has been imported.")

        return self.model

    def vgg16_model(self):
        """Loads the VGG-16 model"""

        pass

    def resnet50_model(self):
        """Loads the ResNet-50 model"""

        pass

    def inceptionv3_model(self):
        """Loads the Inception-V3 model"""

        pass

    def store_visualized_features(self):
        """Stores the visualized features"""

        self.features = []
        self.labels = []

        for images, labels in self.inherited_data(): # This line
            with torch.no_grad():
                print("Features being stored...")
                self.outputs = self.model(images)
                self.features.append(self.model(images))
                self.labels.append(labels)
        
        print('FEATURES STORED SUCCESSFULLY!')
        print(images.shape)
        print(labels.shape)