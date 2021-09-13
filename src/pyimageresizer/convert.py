import os
import pathlib

from PIL import Image

from . preset import Preset

def convert_resolution(path_to_file: str, preset: Preset):
    """Convert the image size and resolution according
    the to bounds defined within preset.

    In all cases, the aspect ratio of the source image is 
    preserved.

    If preset.bounds is not set, do not resize.
    The path to the image is returned.
    """
    with Image.open(path_to_file) as image:
        src_width, src_height = image.size
        aspect_ratio = src_width  / src_height

        if preset.bounds != (None, None):
            target_width, target_height = preset.bounds
            if target_width is None:
                # scale width relative to given height
                target_width = int(target_height * aspect_ratio)
                image = image.resize((target_width, target_height))
            elif target_height is None:
                # scale height relative to given width
                target_height = int(target_width / aspect_ratio)
                image = image.resize((target_width, target_height))

        root = os.path.dirname(path_to_file)
        filename = os.path.basename(path_to_file)
        target_folder = os.path.join(root, preset.name)
        pathlib.Path(target_folder).mkdir(parents=True, exist_ok=True)
        target = os.path.join(target_folder, filename)

        if preset.dpi is not None:
            image.save(target, dpi=(preset.dpi,preset.dpi))
        else:
            image.save(target)
        return target