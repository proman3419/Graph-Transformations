from typing import List
from Graph import Graph
from Production import Production
from Vertex import Vertex
from Edge import Edge


class P7 (Production):
    @staticmethod
    def apply(vertices: List[Vertex], graph: Graph):
        if vertices[0].label == 'F':
            new_vertex = graph.create_add_vertex('F', vertices[0].attributes)

            edges_to_del = []
            edges_to_add = []
            for edge in graph.edges.values():
                edge_to_del_flag = False

                if edge.label == 'd' and \
                   edge.vertex_to_index == vertices[0].index:
                    edge_to_add = Edge(graph.next_edge_index(), edge.label,
                                       edge.vertex_from_index, new_vertex.index,
                                       edge.attributes)
                    edges_to_add.append(edge_to_add)
                    edge_to_del_flag = True

                if edge.label == 'd' and \
                   edge.vertex_from_index == vertices[0].index:
                    edge_to_add = Edge(graph.next_edge_index(), edge.label,
                                       new_vertex.index, edge.vertex_to_index,
                                       edge.attributes)
                    edges_to_add.append(edge_to_add)
                    edge_to_del_flag = True

                if edge_to_del_flag:
                    edges_to_del.append(edge)
            
            for edge in edges_to_del:
                graph.remove_edge(edge)

            for edge in edges_to_add:
                graph.add_edge(edge)

            graph.remove_vertex(vertices[0])

    @staticmethod
    def description() -> str:
        return ('name: P7\n'
                'L: (F)\n'
                "P: (F) --d--> (F')\n"
                """c: {((d, in, 0): (F', Z, d, in)),
    ((d, out, 0): (F', P, d, out)),
    CopyRest}\n""")
