from dataclasses import dataclass

@dataclass
class Preset:
    name: str
    description: str = ""
    dpi: int = None
    bounds: tuple = (None, None)
