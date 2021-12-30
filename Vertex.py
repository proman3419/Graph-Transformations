from typing import *


class Vertex:
    def __init__(self, index: int, label: str):
        self.index = index
        self.label = label
        self.attributes = {}
        self.edges_indexes = []

    def _add_edge(self, edge_index):
        self.edges.append(edge_index)
