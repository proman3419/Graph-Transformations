from typing import List
from Graph import Graph
from Production import Production
from Vertex import Vertex


class P1(Production):
    @staticmethod
    def apply(vertices: List[Vertex], graph: Graph):
        if vertices[0] == 'Z':
            graph.create_add_edge('d', vertices[0], graph.create_add_vertex('F'))

    @staticmethod
    def description() -> str:
        return ('name: P1\n'
                'L: (Z)\n'
                'P: (Z) --d--> (F)\n'
                'c: {CopyRest}\n')
