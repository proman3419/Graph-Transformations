from typing import List
from Graph import Graph
from Production import Production
from Vertex import Vertex


class P6(Production):
    @staticmethod
    def apply(vertices: List[Vertex], graph: Graph):
        if vertices[0].label == 'Z':
            new_vertex_f_index = len(graph.vertices)
            graph.create_add_vertex('F')
            graph.create_add_edge('d', vertices[0], 
                                  graph.vertices[new_vertex_f_index])
            graph.create_add_edge('d', graph.vertices[new_vertex_f_index], 
                                  graph.create_add_vertex('P'))
            graph.create_add_edge('d', graph.vertices[new_vertex_f_index], 
                                  graph.create_add_vertex('P'))

    @staticmethod
    def description() -> str:
        return ('name: P6\n'
                'L: (Z)\n'
                """P: (Z) --d--> (F) --d--> (P)
               \\---d---> (P)\n"""
                'c: {CopyRest}\n')

    @staticmethod
    def to_string():
        return "P6"
