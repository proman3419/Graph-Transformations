from typing import List
from Graph import Graph
from Production import Production
from Vertex import Vertex


class P4(Production):
    @staticmethod
    def get_vertices_number() -> int:
        return 2

    @staticmethod
    def apply(vertices: List[Vertex], graph: Graph):
        if vertices[0].label == 'Z' and vertices[1].label == 'O':
            from_vertex = vertices[0]
            to_vertex = vertices[1]
            graph.create_add_edge('d', from_vertex, to_vertex)

    @staticmethod
    def description() -> str:
        return ('name: P4\n'
                'L: (Z)        (O)\n'
                'P: (Z) --d--> (O)\n'
                'c: {CopyRest}\n')

    @staticmethod
    def to_string():
        return "P4"
