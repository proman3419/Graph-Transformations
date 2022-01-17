from typing import List
from Graph import Graph
from Production import Production
from Vertex import Vertex
from Edge import Edge


class P8(Production):
    @staticmethod
    def apply(vertices: List[Vertex], graph: Graph):
        if vertices[0].label == 'F':
            new_vertex_f_index = len(graph.vertices)
            graph.create_add_vertex('F')
            left_vertex = vertices[0]

            temp_edges = []
            for key, edge in graph.edges.items():
                if key[1] == left_vertex.index and edge.label == 'd':
                    temp_edges.append(Edge(graph.next_edge_index(), 'd', edge.vertex_from_index, new_vertex_f_index, {}))

                if key[0] == left_vertex.index and edge.label == 'd':
                    temp_edges.append(Edge(graph.next_edge_index(), 'd', new_vertex_f_index, edge.vertex_to_index, {}))

            for edge in temp_edges: graph.add_edge(edge)

            graph.add_edge(Edge(graph.next_edge_index(), 'd', left_vertex.index, new_vertex_f_index, {}))
            graph.add_edge(Edge(graph.next_edge_index(), 'd', new_vertex_f_index, left_vertex.index, {}))

    @staticmethod
    def description() -> str:
        return ('name: P8\n'
                'L: (F)\n'
                "P: (F) --d--> (F')\n"
                "    \\---<-d---/\n"
                """c: {((d, in, 0): (F', Z, d, in)),
    ((d, out, 0): (F', P, d, out)),
    CopyRest}\n"""
    "where ' is used for temporary indexing only\n")

    @staticmethod
    def to_string():
        return "P8"
