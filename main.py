from Graph import Graph
from P1 import P1
from P2 import P2
from P3 import P3
from Visualization import Visualization

if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex('Z', {'source_type': 'apple'})

    P1.apply([graph.vertices[0]], graph)
    print(graph)

    P2.apply([graph.vertices[0], graph.vertices[1]], graph)
    print(graph)

    graph.add_vertex('Z')
    P3.apply([graph.vertices[0], graph.vertices[2]], graph)
    print(graph)

    visualization = Visualization(graph)
    visualization.run()
