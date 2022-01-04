from dataclasses import dataclass
from typing import Dict


@dataclass
class Vertex:
    index: int
    label: str
    attributes: Dict[str, str]
