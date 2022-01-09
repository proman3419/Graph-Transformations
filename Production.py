from abc import ABC, abstractmethod
from typing import List
from Graph import Graph
from Vertex import Vertex


class Production(ABC):
    @staticmethod
    def get_vertices_number() -> int:
        return 1

    @staticmethod
    @abstractmethod
    def apply(vertices: List[Vertex], graph: Graph):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def description() -> str:
        raise NotImplementedError
