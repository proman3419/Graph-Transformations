from typing import List
from Graph import Graph
from Production import Production
from Vertex import Vertex


class P2(Production):
    @staticmethod
    def apply(vertices: List[Vertex], graph: Graph):
        from_vertex = vertices[0]
        to_vertex = vertices[1]
        edge = graph.edges[(from_vertex.index, to_vertex.index)]
        graph.remove_edge(edge)
