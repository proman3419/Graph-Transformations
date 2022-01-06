from bokeh.io import show
from bokeh.layouts import column
from bokeh.models import Button
from bokeh.plotting import from_networkx
import networkx as nx
from bokeh.models.graphs import from_networkx
from bokeh.models import MultiLine, Circle, TapTool, HoverTool, BoxSelectTool
from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.events import Tap


class Visualization:
    def __init__(self, graph):
        self.selected_nodes = []
        self.graph = self._convert_graph(graph)
        self.button = Button(label="Click on the button",
                             button_type="danger")
        self._create_buttons()

        self.plot = figure(width=800, height=600, x_range=(-1.2, 1.2), y_range=(-1.2, 1.2),
                           x_axis_location=None, y_axis_location=None, toolbar_location=None,
                           title="Graph Interaction Demo", background_fill_color="#efefef")
        self.plot.grid.grid_line_color = None

        self.graph_renderer = from_networkx(self.graph, nx.spring_layout, scale=1, center=(0, 0))

        self.source = self.graph_renderer.node_renderer.data_source

        self.graph_renderer.node_renderer.glyph = Circle(size=15, fill_color="line_color")
        self.graph_renderer.edge_renderer.glyph = MultiLine(line_color="black",
                                                            line_alpha=0.8, line_width=1.5)

        TOOLTIPS = [
            ("Index", "@index"),
        ]

        self.plot.add_tools(HoverTool(tooltips=TOOLTIPS), TapTool(), BoxSelectTool())
        self.plot.renderers.append(self.graph_renderer)
        taptool = self.plot.select(type=TapTool)
        self.plot.on_event(Tap, self.clicking_update)
        self.layout = column(self.button, self.plot)

    def choose_node_outline_colors(self, nodes_clicked):
        outline_colors = []
        for node in self.graph.nodes():
            if str(node) in nodes_clicked:
                outline_colors.append('pink')
            else:
                outline_colors.append('black')
        return outline_colors

    def clicking_update(self, event):
        nodes_clicked_ints = self.source.selected.indices
        print(nodes_clicked_ints)
        nodes_clicked = list(map(str, nodes_clicked_ints))
        self.source.data['line_color'] = self.choose_node_outline_colors(nodes_clicked)

    def cos(self):
        self.graph.add_node(4)
        self.graph.add_edge(3, 4)
        self.graph.add_edge(4, 2)

        self.plot = figure(width=800, height=600, x_range=(-1.2, 1.2), y_range=(-1.2, 1.2),
                           x_axis_location=None, y_axis_location=None, toolbar_location=None,
                           title="Graph Interaction Demo", background_fill_color="#efefef",
                           tooltips="index: @index, label: @label")
        self.plot.grid.grid_line_color = None

        self.graph_renderer = from_networkx(self.graph, nx.spring_layout, scale=1, center=(0, 0))

        self.source = self.graph_renderer.node_renderer.data_source

        self.graph_renderer.node_renderer.glyph = Circle(size=15, fill_color="line_color")
        self.graph_renderer.edge_renderer.glyph = MultiLine(line_color="black",
                                                            line_alpha=0.8, line_width=1.5)

        TOOLTIPS = [
            ("Index", "@index"),
        ]

        self.plot.add_tools(HoverTool(tooltips=TOOLTIPS), TapTool(), BoxSelectTool())
        self.plot.renderers.append(self.graph_renderer)
        taptool = self.plot.select(type=TapTool)
        self.plot.on_event(Tap, self.clicking_update)
        self.layout = column(self.button, self.plot)
        curdoc().clear()
        curdoc().add_root(self.layout)

    @staticmethod
    def _convert_graph(graph):
        new_graph = nx.Graph()

        for vertex in graph.edges:
            new_graph.add_node(vertex[0])
            new_graph.add_edge(vertex[0], vertex[1])

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
