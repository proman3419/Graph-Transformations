from dataclasses import dataclass
from typing import Dict


@dataclass
class Vertex:
    index: int
    label: str
    attributes: Dict[str, str]

    def to_color(self) -> str:
        if self.label == 'Z': return '#53ad61'
        if self.label == 'F': return '#c17feb'
        if self.label == 'P': return '#fcba03'
        if self.label == 'O': return '#4b7fc4'

    def __str__(self):
        return str(self.index) + ' ' + self.label
