from typing import *
from itertools import count
from Vertex import *
from Edge import *
from Production import *


class Graph:
    def __init__(self):
        self.edges = {}
        self.vertices = {}
        self.vertex_index_generator = count(start=0, step=1)

    def _add_vertex(self, label: str):
        vertex = Vertex(next(self.vertex_index_generator), label)
        self.vertices[vertex.index] = vertex

    def _add_edge(self, index: int, label: str, vertex_start: Vertex,
                  vertex_end: Vertex):
        edge = Edge(index, label, vertex_start, vertex_end)
        self.edges[edge.index] = edge

    def apply_production(production: Production, vertices_indexes: List[int]):
        vertices = [self.vertices[index] for index in vertices_indexes]
        production.apply(self, vertices)
