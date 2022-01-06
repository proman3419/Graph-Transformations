from typing import List

from Graph import Graph
from Production import Production
from Vertex import Vertex


class P4(Production):
    @staticmethod
    def apply(vertices: List[Vertex], graph: Graph):
        from_vertex = vertices[0]
        to_vertex = vertices[1]
        graph.add_edge('d', from_vertex, to_vertex)
