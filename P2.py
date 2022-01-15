from typing import List
from Graph import Graph
from Production import Production
from Vertex import Vertex


class P2(Production):
    @staticmethod
    def get_vertices_number() -> int:
        return 2

    @staticmethod
    def apply(vertices: List[Vertex], graph: Graph):
        from_vertex = vertices[0]
        to_vertex = vertices[1]
        edge = graph.edges[(from_vertex.index, to_vertex.index)]
        graph.remove_edge(edge)

    @staticmethod
    def description() -> str:
        return ('name: P2\n'
                'L: ( ) -----> ( )\n'
                'P: ( )        ( )\n'
                'c: {CopyRest}\n')
