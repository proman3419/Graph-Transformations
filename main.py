from Graph import *
from P1 import *


if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex('Z')
    P1.apply([graph.vertices[0]], graph)
    P1.apply([graph.vertices[0]], graph)
    P1.apply([graph.vertices[0]], graph)
    print(graph)
