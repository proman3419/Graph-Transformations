from Graph import Graph
from P1 import P1
from P2 import P2
from P3 import P3
from P4 import P4
from P5 import P5
from P6 import P6
from P7 import P7
from P8 import P8


if __name__ == '__main__':
    graph = Graph()
    graph.create_add_vertex('Z')
    P1.apply([graph.vertices[0]], graph)
    print(graph)

    P2.apply([graph.vertices[0], graph.vertices[1]], graph)
    print(graph)

    graph.create_add_vertex('Z')
    P3.apply([graph.vertices[0], graph.vertices[2]], graph)
    print(graph)

    graph = Graph()
    graph.create_add_vertex('Z')
    graph.create_add_vertex('F')
    graph.create_add_vertex('O')
    graph.create_add_edge('d', graph.vertices[0], graph.vertices[1])
    graph.create_add_edge('d', graph.vertices[1], graph.vertices[2])
    print(graph)
    P7.apply([graph.vertices[1]], graph)
    print(graph)
    P8.apply([graph.vertices[3]], graph)
    print(graph)

    print(P1.description())
    print(P2.description())
    print(P3.description())
    print(P4.description())
    print(P5.description())
    print(P6.description())
    print(P7.description())
    print(P8.description())
