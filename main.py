from Graph import Graph
from Visualization import Visualization


graph = Graph()
graph.create_add_vertex('Z')
graph.create_add_vertex('F')
graph.create_add_vertex('P')
graph.create_add_vertex('O')
graph.create_add_edge('d', graph.vertices[0], graph.vertices[1])
graph.create_add_edge('d', graph.vertices[1], graph.vertices[2])
graph.create_add_edge('d', graph.vertices[2], graph.vertices[3])
graph.create_add_edge('d', graph.vertices[0], graph.vertices[3])

visualization = Visualization(graph)
visualization.run()
