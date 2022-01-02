from typing import List

from Graph import Graph
from Production import Production
from Vertex import Vertex


class P3(Production):
    @staticmethod
    def apply(vertices: List[Vertex], graph: Graph):
        new_vertex = graph.add_vertex('F')
      
        for vertex in vertices:
            if vertex.label == 'Z':
                graph.add_edge('d', vertex, new_vertex)
