import os
import pathlib

from PIL import Image

from . preset import Preset

def convert_resolution(path_to_file: str, preset: Preset):
    """Convert the image size and resolution according
    the to bounds defined within preset.

    If preset.bounds is not set, do not resize.
    The path to the image is returned.
    """
    image = Image.open(path_to_file)
    root = os.path.dirname(path_to_file)
    filename = os.path.basename(path_to_file)
    target_folder = os.path.join(root, preset.name)
    pathlib.Path(target_folder).mkdir(parents=True, exist_ok=True)
    target = os.path.join(target_folder, filename)
    if preset.bounds != (None, None):
        image.thumbnail(preset.bounds, Image.ANTIALIAS)
    if preset.dpi is not None:
        image.save(target, dpi=(preset.dpi,preset.dpi))
    else:
        image.save(target)
    return target