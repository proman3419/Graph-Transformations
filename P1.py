from typing import List
from Graph import Graph
from Production import Production
from Vertex import Vertex


class P1 (Production):
    @staticmethod
    def apply(vertices: List[Vertex], graph: Graph):
        graph.add_edge('d', vertices[0], graph.add_vertex('F'))
