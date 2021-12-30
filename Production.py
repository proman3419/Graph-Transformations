from abc import ABC, abstractmethod
from typing import *
from Graph import *
from Vertex import *


class Production (ABC):
    @staticmethod
    @abstractmethod
    def apply(vertices: List[Vertex], graph: Graph):
        raise NotImplementedError