import tkinter as tk
import torch
import torchvision.models as models
import os
from tkinter import filedialog as fd
from torchvision import datasets, transforms
from PIL import Image

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

        self.heading_Label = tk.Label(
            master, text="Data Import Section", font=("Arial", 30)
        )
        self.heading_Label.pack(pady=20)

        self.data_Import_Button = tk.Button(
            master, text="Dataset Import", command=self.load_data, width=15, height=2
        )
        self.data_Import_Button.pack(anchor="center", pady=50)

        self.data_Transform_Button = tk.Button(
            master, text="Transform Data", command=self.get_data_transformed, width=15, height=2
        )
        self.data_Transform_Button.pack(anchor="center", pady=50)

        self.data_Imported_Label = tk.Label(
            master,
            text="",
            font=("Arial", 12),
        )
        self.data_Imported_Label.pack(pady=10)

        # self.visualize_model_button = ttk.Button(master, text="Visualize Model", command=self.visualize_model, state='disabled')
        # self.visualize_model_button.pack()

        self.canvas = tk.Canvas(master, width=700, height=500)
        self.canvas.pack()

    def load_data(self):
        """Loading the data from the directory"""

        self.data_Import_Button["state"] = "normal"

        self.image_data_paths = fd.askdirectory()

        self.data_Imported_Label.config(
            text="Data Imported from {}.".format(
                self.image_data_paths
            )
        )

    def get_directory(self):
        """Returns the directory path of the dataset"""

        return self.image_data_paths

    def get_data_transformed(self):
        """Returns the transformed dataset"""

        self.data_Transform_Button["state"] = "normal"
        
        self.dataset = datasets.ImageFolder(root=self.get_directory(), transform=self.preprocess_mobilenetv3())

        self.dataloader = torch.utils.data.DataLoader(self.dataset, batch_size=32, shuffle=False)

        print("Dataset transformation complete. You can now move on to the next step.")

        return self.dataloader

    def preprocess_mobilenetv3(self):
        """Preprocesses the input image for MobileNet-V3"""

        IMG_HEIGHT = 256
        IMG_WIDTH = 256

        self.transform = transforms.Compose(
            [
                transforms.ToTensor(),  # Convert the image to PyTorch Tensor data type
                transforms.Resize(
                    (IMG_HEIGHT, IMG_WIDTH), interpolation=Image.BILINEAR
                ),  # Resize the images
                transforms.CenterCrop(
                    224
                ),  # Crop the images to 224x224 about the center
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
                ),  # Normalize the images
            ]
        )

        return self.transform

    # def get_model_graph(self):
    #     """Generates a random 3D graph"""

    #     graph = np.random.rand(500, 500, 3)
    #     return graph
