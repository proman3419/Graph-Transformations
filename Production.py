from abc import ABC, abstractmethod
from typing import *
from Graph import *
from Vertex import *


class Production (ABC):
    def __init__(self):
        pass

    @abstractmethod
    def apply(self, vertices: List[Vertex], graph: Graph):
        raise NotImplementedError
