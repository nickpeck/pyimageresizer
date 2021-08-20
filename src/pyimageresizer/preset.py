from dataclasses import dataclass, field
from typing import Any

@dataclass
class Preset:
    name: str
    description: str
    dpi: int
    bounds: tuple = (None, None)