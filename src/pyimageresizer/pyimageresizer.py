"""Main GUI for PyImageResizer
"""
import os
import tkinter as tk
import traceback

import pygubu
from tkinterdnd2 import DND_ALL

from . convert import convert_resolution
from . preset import Preset

VALID_EXTS = [".png", ".bmp", ".jpg", ".jpeg", ".gif", ".tiff"]

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "pyimageresizer.ui")

DPI_PRESETS = {p.description:p for p in [
    Preset(
        name="72 dpi",
        description="low (emails) 72 dpi",
        dpi=72
    ),
    Preset(
        name="300 dpi",
        description="high (print) 300 dpi",
        dpi=300
    ),
    Preset(
        name="same dpi",
        description="as-is",
        dpi=None
    ),
]}

BOUNDS_PRESETS = {p.description:p for p in [
    Preset(
        name="height=1024",
        description="height is 1024px",
        bounds=(None, 1024)
    ),
    Preset(
        name="height=800",
        description="height is 800px",
        bounds=(None, 800)
    ),
    Preset(
        name="width=768",
        description="width is 768px",
        bounds=(768, None)
    ),
    Preset(
        name="width=600",
        description="width is 600px",
        bounds=(600, None)
    ),
    Preset(
        name="same size",
        description="size remains the same",
        bounds=(None,None)
    ),
]}

class PyimageresizerApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('toplevel1', master)
        self.mainwindow.resizable(width=False, height=False)

        # set the preset options
        self.dpi_combo_sel = builder.get_object('dpiComboSel', master)
        self.dpi_combo_sel['values'] = list(DPI_PRESETS.keys())
        self.dpi_combo_sel.current(0)

        self.bounds_combo_sel = builder.get_object('boundsComboSel', master)
        self.bounds_combo_sel['values'] = list(BOUNDS_PRESETS.keys())
        self.bounds_combo_sel.current(0)

        # bind the scrollpane and the console
        self.console = builder.get_object('console', master)
        self.yscrollbar = builder.get_object('yscrollbar', master)
        self.console['yscrollcommand'] = self.yscrollbar.set
        self.yscrollbar['command'] = self.console.yview

        # load the tknd drag and drop wrapper
        self._load_tkdnd()
        self._bind_dnd()

        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def on_drop(self, event):
        """Handle the drop event. Files are converted according to the
        selected preset and saved in a subfolder dictated by the preset's
        shortname.
        """
        self.log("Batch conversion starting")
        files = self.mainwindow.splitlist(event.data)

        # compose a preset using the selected resolution and bounds
        dpi_preset_name = self.dpi_combo_sel.get()
        dpi_preset = DPI_PRESETS[dpi_preset_name]
        bounds_preset_name = self.bounds_combo_sel.get()
        bounds_preset = BOUNDS_PRESETS[bounds_preset_name]

        preset = Preset(
            name =  "{}-{}".format(dpi_preset.name, bounds_preset.name),
            dpi = dpi_preset.dpi,
            bounds = bounds_preset.bounds
        )

        # walk though the list of files, and the 1st level
        # of any selected directories, converting the images
        path = None
        for file in files:
            if os.path.isdir(file):
                self._convert_folder(file, preset)
            else:
                path = self._convert_image(file, preset)

        self.log("Batch conversion complete")
        # if the selection was of files only,
        # open explorer in the output directory
        if path is not None:
            parent_folder = os.path.dirname(path)
            os.startfile(parent_folder)

    def _convert_folder(self, folder, preset):
        for file in os.listdir(folder):
            if os.path.isdir(file):
                continue
            self._convert_image(os.path.join(folder, file), preset)

    def _convert_image(self, path_to_file, preset):
        ext = os.path.splitext(path_to_file)[1]
        if ext.lower() not in VALID_EXTS:
            self.log("Unsupported image extension : {}".format(ext))
            return None
        try:
            path = convert_resolution(path_to_file, preset)
        except Exception:
            self.log(traceback.format_exc())
            self.log("[WARNING] conversion failed")
        self.log(path)
        return path

    def log(self, *args):
        print(*args)
        for item in args:
            self.console.insert(tk.END,  "\n" + str(item))
            self.console.see(tk.END)

    def _load_tkdnd(self):
        """
        Dynamically load TKDND to enable drag and drop.
        The app will attempt to use the TKDND_PATH env variable,
        if this is set, otherwise, it will assume these are packaged
        within the current module.
        """
        import_path = None
        path_to_tkdnd = os.environ.get("TKDND_PATH")
        if path_to_tkdnd is not None and  os.path.exists(path_to_tkdnd):
            import_path = path_to_tkdnd
        else:
            import_path = PROJECT_PATH
        try:
            self.mainwindow.tk.eval(
                f"global auto_path; lappend auto_path {{{import_path}}}"
            )
            self.mainwindow.tk.call("package", "require", "tkdnd")
        except tk.TclError:
            self.log(traceback.format_exc())
            self.log("[WARNING] TKDND could not be loaded")

    def _bind_dnd(self):
        """
        Binds the drag-and-drop callbacks
        """
        element = self.builder.get_object('dropzone')
        element.drop_target_register(DND_ALL)
        element.dnd_bind("<<Drop>>", self.on_drop)
