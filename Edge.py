from dataclasses import dataclass
from typing import Dict


@dataclass
class Edge:
    index: int
    label: str
    vertex_from_index: int
    vertex_to_index: int
    attributes: Dict[str, str]
