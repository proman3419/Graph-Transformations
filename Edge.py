from typing import *
from Vertex import *


class Edge:
    def __init__(self, index: int, label: str, vertex_start: Vertex,
                 vertex_end: Vertex):
        self.index = index
        self.label = label
        self.attributes = {}
        self.vertex_start = vertex_start
        self.vertex_end = vertex_end
