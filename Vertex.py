from dataclasses import dataclass
from typing import Dict


@dataclass
class Vertex:
    index: int
    label: str
    attributes: Dict[str, str]
    colors = {'Z': '#53ad61', 'F': '#c17feb', 'P': '#fcba03', 'O': '#4b7fc4'}

    def to_color(self) -> str:
        return self.colors[self.label]

    def __str__(self):
        return str(self.index) + ' ' + self.label
