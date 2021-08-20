"""Main entry point when used with PyInstaller
"""
from pyimageresizer.pyimageresizer import PyimageresizerApp

if __name__ == '__main__':
    app = PyimageresizerApp()
    app.run()
