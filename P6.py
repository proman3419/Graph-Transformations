from typing import List

from Graph import Graph
from Production import Production
from Vertex import Vertex


class P6(Production):
    @staticmethod
    def apply(vertices: List[Vertex], graph: Graph):
        new_vertex_f_index = len(graph.vertices)
        graph.add_vertex('F')
        graph.add_edge('d', vertices[0], graph.vertices[new_vertex_f_index])
        graph.add_edge('d', graph.vertices[new_vertex_f_index], graph.add_vertex('P'))
        graph.add_edge('d', graph.vertices[new_vertex_f_index], graph.add_vertex('P'))
