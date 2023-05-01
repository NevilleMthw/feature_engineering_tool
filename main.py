import tkinter as tk
from tkinter import ttk

from dataset_import_window import DatasetImportWindow
from feature_extract_window import FeatureExtractWindow
from feature_selection_window import FeatureSelection

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
