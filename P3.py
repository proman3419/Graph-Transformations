from typing import List
from Graph import Graph
from Production import Production
from Vertex import Vertex


class P3(Production):
    @staticmethod
    def apply(vertices: List[Vertex], graph: Graph):
        if vertices[0].label == 'L':
            new_vertex = graph.create_add_vertex('P')
            graph.create_add_edge('d', vertices[0], new_vertex)

    @staticmethod
    def description() -> str:
        return ('name: P3\n'
                'L: (F)\n'
                'P: (F) --d--> (P)\n'
                'c: {CopyRest}\n')

    @staticmethod
    def to_string():
        return "P3"
