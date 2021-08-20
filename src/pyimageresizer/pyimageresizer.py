"""Main GUI for PyImageResizer
"""

import os
import sys
import subprocess
import tkinter as tk
import tkinter.ttk as ttk

import pygubu
from tkinterdnd2 import DND_ALL

from . convert import convert_resolution
from . preset import Preset

VALID_EXTS = [".png", ".bmp", ".jpg", ".jpeg", ".gif", ".tiff"]

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "pyimageresizer.ui")

PRESETS = {p.description:p for p in [
    Preset(
        name="email 72dpi",
        description="email ( 600 72 dpi)",
        dpi=72,
        bounds=(600, 600)
    ),
    Preset(
        name="5-4",
        description="5:4 (1280x1024 72 dpi)",
        dpi=72,
        bounds=(1280,1024)
    ),
    Preset(
        name="4-3",
        description="4:3 (720x576 72 dpi)",
        dpi=72,
        bounds=(720,576)
    ),
    Preset(
        name="print 300dpi",
        description="print (upscale 300 dpi)",
        dpi=300
    ),
]}

class PyimageresizerApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('toplevel1', master)

        # set the preset options
        self.combo = builder.get_object('combobox2', master)
        self.combo['values'] = list(PRESETS.keys())
        self.combo.current(0)

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
        preset_name = self.combo.get()
        preset = PRESETS[preset_name]
        path = None
        for file in files:
            if os.path.isdir(file):
                continue
            ext = os.path.splitext(file)[1]
            if ext.lower() not in VALID_EXTS:
                self.log("Unsupported image extension : {}".format(ext))
                continue
            path = convert_resolution(file, preset)
            self.log(path)
        if path is not None:
            self.log("Batch conversion complete")
            parent_folder = os.path.dirname(path)
            os.startfile(parent_folder)

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
        except tk.TclError as e:
            self.log("[WARNING] TKDND could not be loaded")

    def _bind_dnd(self):
        """
        Binds the drag-and-drop callbacks
        """
        element = self.builder.get_object('dropzone')
        element.drop_target_register(DND_ALL)
        element.dnd_bind("<<Drop>>", self.on_drop)