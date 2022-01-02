from dataclasses import dataclass


@dataclass
class Edge:
    index: int
    label: str
    vertex_from_index: int
    vertex_to_index: int
