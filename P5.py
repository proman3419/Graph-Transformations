from typing import List

from Graph import Graph
from Production import Production
from Vertex import Vertex


class P5(Production):
    @staticmethod
    def apply(vertices: List[Vertex], graph: Graph):
        for vertex in graph.vertices.values():
            if vertex.label == 'O':
                graph.create_add_edge('d', vertices[0], vertex)
                break

    @staticmethod
    def description() -> str:
        return ('name: P5\n'
                'L: (P)\n'
                'P: (P) --d--> (O)\n'
                'c: {CopyRest}\n')
