from typing import *
from dataclasses import dataclass


@dataclass
class Edge:
    index: int
    label: str
    vertex_start_index: int
    vertex_end_index: int
