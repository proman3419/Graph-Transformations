from typing import *
from itertools import count
from Vertex import *
from Edge import *


class Graph:
    def __init__(self):
        self.edges = {}
        self.vertices = {}
        self.edge_index_generator = count(start=0, step=1)
        self.vertex_index_generator = count(start=0, step=1)
