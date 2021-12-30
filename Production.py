from typing import *
from abc import ABC, abstractmethod
from Graph import *


class Production (ABC):
    def __init__(self):
        pass

    @abstractmethod
    def apply(self, vertices: List[Vertex]):
        raise NotImplementedError
