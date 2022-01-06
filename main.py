from Graph import Graph
from P1 import P1
from P2 import P2
from P3 import P3
from P7 import P7


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

    graph = Graph()
    graph.add_vertex('Z')
    graph.add_vertex('F')
    graph.add_vertex('O')
    graph.add_edge('d', graph.vertices[0], graph.vertices[1])
    graph.add_edge('d', graph.vertices[1], graph.vertices[2])
    print(graph)
    P7.apply([graph.vertices[1]], graph)
    print(graph)
