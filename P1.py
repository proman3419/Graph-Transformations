from typing import *
from Graph import *
from Production import *
from Vertex import *


class P1 (Production):
    @staticmethod
    def apply(vertices: List[Vertex], graph: Graph):
        graph.add_edge('d', vertices[0], graph.add_vertex('F'))
