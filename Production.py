from abc import ABC, abstractmethod
from typing import List
from Graph import Graph
from Vertex import Vertex


class Production (ABC):
    @staticmethod
    @abstractmethod
    def apply(vertices: List[Vertex], graph: Graph):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def description() -> str:
        raise NotImplementedError
