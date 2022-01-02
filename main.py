from Graph import *
from P1 import *
from P2 import *
from P3 import *


if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex('Z')
    P1.apply([graph.vertices[0]], graph)
    print(graph)

    P2.apply([graph.vertices[0], graph.vertices[1]], graph)
    print(graph)

    graph.add_vertex('Z')
    P3.apply([graph.vertices[0], graph.vertices[2]], graph)
    print(graph)
