from itertools import count
from typing import Dict
from Vertex import Vertex
from Edge import Edge


class Graph:
    def __init__(self):
        self.edges = {}
        self.vertices = {}
        self.edge_index_generator = count(start=0, step=1)
        self.vertex_index_generator = count(start=0, step=1)

    def next_edge_index(self) -> int:
        return next(self.edge_index_generator)

    def next_vertex_index(self) -> int:
        return next(self.vertex_index_generator)

    def add_vertex(self, label: str, attributes: Dict[str, str]={}) -> Vertex:
        vertex = Vertex(self.next_vertex_index(), label, attributes)
        self.vertices[vertex.index] = vertex
        return vertex

    def add_edge(self, label: str, vertex_from: Vertex, vertex_to: Vertex, attributes: Dict[str, str]={}) -> Edge:
        edge = Edge(self.next_edge_index(), label, vertex_from.index, 
                    vertex_to.index, attributes)
        self.edges[(vertex_from.index, vertex_to.index)] = edge
        return edge

    def __str__(self):
        return self.edges.__str__() + '\n' + self.vertices.__str__() + '\n'
