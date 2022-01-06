from typing import List
from Graph import Graph
from Production import Production
from Vertex import Vertex


class P3(Production):
    @staticmethod
    def apply(vertices: List[Vertex], graph: Graph):
        new_vertex = graph.create_add_vertex('F')
        graph.create_add_edge('d', vertices[0], new_vertex)
        
        for vertex in graph.vertices.values():
            if vertex.label == 'Z':
                graph.create_add_edge('d', vertex, new_vertex)

    @staticmethod
    def description() -> str:
        return ('name: P3\n'
                'L:\n'
                'P:\n'
                'c:\n')
