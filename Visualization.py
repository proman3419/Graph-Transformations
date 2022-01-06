from bokeh.io import show, save, curdoc
from bokeh.layouts import column, row
from bokeh.models import Button, CustomJS, Circle, MultiLine
import networkx as nx
from bokeh.plotting import figure, from_networkx

class Visualization:
    def __init__(self, graph):
        self.graph = graph
        self.button = Button(label="Click on the button",
                        button_type="danger")
        self._create_buttons()

        self.graph = self._convert_graph(self.graph)

        self.plot = figure(width=800, height=600, x_range=(-1.2, 1.2), y_range=(-1.2, 1.2),
                      x_axis_location=None, y_axis_location=None, toolbar_location=None,
                      title="Graph Interaction Demo", background_fill_color="#efefef",
                      tooltips="index: @index, label: @label")
        self.plot.grid.grid_line_color = None

        self.graph_renderer = from_networkx(self.graph, nx.spring_layout, scale=1, center=(0, 0))
        self.graph_renderer.node_renderer.glyph = Circle(size=15, fill_color="lightblue")
        self.graph_renderer.edge_renderer.glyph = MultiLine(line_color="black",
                                                       line_alpha=0.8, line_width=1.5)

        self.plot.renderers.append(self.graph_renderer)

        self.layout = column(self.button, self.plot)

    def cos(self):
        self.graph.add_node(4)
        self.graph.add_edge(3, 4)

        self.plot = figure(width=800, height=600, x_range=(-1.2, 1.2), y_range=(-1.2, 1.2),
                      x_axis_location=None, y_axis_location=None, toolbar_location=None,
                      title="Graph Interaction Demo", background_fill_color="#efefef",
                      tooltips="index: @index, label: @label")
        self.plot.grid.grid_line_color = None

        self.graph_renderer = from_networkx(self.graph, nx.spring_layout, scale=1, center=(0, 0))
        self.graph_renderer.node_renderer.glyph = Circle(size=15, fill_color="lightblue")
        self.graph_renderer.edge_renderer.glyph = MultiLine(line_color="black",
                                                       line_alpha=0.8, line_width=1.5)

        self.layout.children[1] = self.plot

        self.plot.renderers.append(self.graph_renderer)

        curdoc().clear()
        curdoc().add_root(self.layout)

    @staticmethod
    def _convert_graph(graph):
        new_graph = nx.Graph()

        for vertex in graph.edges:
            new_graph.add_node(vertex[0])
            new_graph.add_edge(vertex[0],vertex[1])

        return new_graph

    def _add_info(self):
        index = []
        label = []

    def _create_buttons(self):
        self.button.on_click(self.cos)

    def run(self):
        curdoc().add_root(self.layout)
        show(self.layout)
        # show(self.layout)