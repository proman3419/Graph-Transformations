from typing import List
from Graph import Graph
from Production import Production
from Vertex import Vertex
from copy import deepcopy


class P7 (Production):
    @staticmethod
    def apply(vertices: List[Vertex], graph: Graph):
        if vertices[0].label == 'F':
            new_vertex = graph.add_vertex('F', vertices[0].attributes)

            edges_to_del = []
            edges_to_add = []
            for edge in graph.edges.values():
                edge_to_del_flag = False

                if edge.label == 'd' and \
                   edge.vertex_to_index == vertices[0].index:
                    edge_to_add = deepcopy(edge)
                    edge_to_add.index = graph.next_edge_index()
                    edge_to_add.vertex_to_index = new_vertex.index
                    edges_to_add.append(edge_to_add)
                    edge_to_del_flag = True

                if edge.label == 'd' and \
                   edge.vertex_from_index == vertices[0].index:
                    edge_to_add = deepcopy(edge)
                    edge_to_add.index = graph.next_edge_index()
                    edge_to_add.vertex_from_index = new_vertex.index
                    edges_to_add.append(edge_to_add)
                    edge_to_del_flag = True

                if edge_to_del_flag:
                    edges_to_del.append(edge)
            
            for edge in edges_to_del:
                del graph.edges[(edge.vertex_from_index, edge.vertex_to_index)]

            for edge in edges_to_add:
                graph.edges[(edge.vertex_from_index, edge.vertex_to_index)] = edge

            del graph.vertices[vertices[0].index]
