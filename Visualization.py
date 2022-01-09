from bokeh.io import show
from bokeh.layouts import column
from bokeh.models import Button, Dropdown
from bokeh.plotting import from_networkx
import networkx as nx
from bokeh.models.graphs import from_networkx
from bokeh.models import MultiLine, Circle, TapTool, HoverTool, BoxSelectTool
from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.events import Tap
from P1 import P1
from P2 import P2
from P3 import P3
from P4 import P4
from P5 import P5
from P6 import P6
from P7 import P7


class Visualization:
    production_classes_by_names = {
        "Production 1": P1,
        "Production 2": P2,
        "Production 3": P3,
        "Production 4": P4,
        "Production 5": P5,
        "Production 6": P6,
        "Production 7": P7,
        "Production 8": None,
    }
    production_selected = None
    vertices_chosen = set()

    def __init__(self, graph):
        self.selected_nodes = []
        self.graph = graph
        self.networkx_graph = self._convert_graph()
        self._create_buttons()

        self.plot = figure(width=800, height=600, x_range=(-1.2, 1.2), y_range=(-1.2, 1.2),
                           x_axis_location=None, y_axis_location=None, toolbar_location=None,
                           title="Graph Interaction Demo", background_fill_color="#efefef")
        self.plot.grid.grid_line_color = None
        self.graph_renderer = from_networkx(self.networkx_graph, nx.spring_layout, scale=1, center=(0, 0))

        self.source = self.graph_renderer.node_renderer.data_source

        self.graph_renderer.node_renderer.glyph = Circle(size=15, fill_color="blue")
        self.graph_renderer.edge_renderer.glyph = MultiLine(line_color="black",
                                                            line_alpha=0.8, line_width=1.5)

        TOOLTIPS = [
            ("Index", "@index"),
        ]

        self.plot.add_tools(HoverTool(tooltips=TOOLTIPS), TapTool(), BoxSelectTool())
        self.plot.renderers.append(self.graph_renderer)
        taptool = self.plot.select(type=TapTool)
        self.plot.on_event(Tap, self.clicking_update)
        self.layout = column(self.dropdown, self.plot)

    def _create_buttons(self):
        self.menu = [("Production 1", "Production 1"), ("Production 2", "Production 2"),
                     ("Production 3", "Production 3"), ("Production 4", "Production 4"),
                     ("Production 5", "Production 5"), ("Production 6", "Production 6"),
                     ("Production 7", "Production 7"), ("Production 8", "Production 8")]

        self.dropdown = Dropdown(label="Productions", button_type="warning", menu=self.menu)
        self.dropdown.on_click(self._dropdown_update)

    def _dropdown_update(self, event):
        self.dropdown.label = event.item
        self.production_selected = self.production_classes_by_names.get(event.item)
        self.vertices_chosen.clear()
        print(self.dropdown.label)
        print(self.production_selected)
        print(self.vertices_chosen)

    def clicking_update(self, event):
        node_clicked_list = self.source.selected.indices
        print(node_clicked_list)
        print(list(self.networkx_graph.nodes()))
        print(self.graph.vertices)
        if node_clicked_list and self.production_selected:
            vertex_index = list(self.networkx_graph.nodes())[node_clicked_list[0]]
            print('indeksik ', vertex_index)
            self.vertices_chosen.add(vertex_index)
            if len(self.vertices_chosen) == self.production_selected.get_vertices_number():
                self.apply_production()

    def apply_production(self):
        print('============================')
        print(self.vertices_chosen)
        print(self.graph.vertices)
        print(self.graph.edges)
        print([self.graph.vertices[id] for id in self.vertices_chosen])
        print("============================")
        #TODO (2,3) is not proper, check 2 combinations
        self.production_selected.apply([self.graph.vertices[id] for id in self.vertices_chosen], self.graph)
        self.networkx_graph = self._convert_graph()
        self.production_selected = None
        self.vertices_chosen.clear()
        self.dropdown.label = "Productions"

        self.plot = figure(width=800, height=600, x_range=(-1.2, 1.2), y_range=(-1.2, 1.2),
                           x_axis_location=None, y_axis_location=None, toolbar_location=None,
                           title="Graph Interaction Demo", background_fill_color="#efefef")
        self.plot.grid.grid_line_color = None
        self.graph_renderer = from_networkx(self.networkx_graph, nx.spring_layout, scale=1, center=(0, 0))
        self.source = self.graph_renderer.node_renderer.data_source
        self.graph_renderer.node_renderer.glyph = Circle(size=15, fill_color="blue")
        self.graph_renderer.edge_renderer.glyph = MultiLine(line_color="black",
                                                            line_alpha=0.8, line_width=1.5)

        self.layout.children[1] = self.plot
        TOOLTIPS = [
            ("Index", "@index"),
        ]

        self.plot.add_tools(HoverTool(tooltips=TOOLTIPS), TapTool(), BoxSelectTool())
        self.plot.renderers.append(self.graph_renderer)
        taptool = self.plot.select(type=TapTool)
        self.plot.on_event(Tap, self.clicking_update)
        curdoc().clear()
        curdoc().add_root(self.layout)


    def _convert_graph(self):
        new_graph = nx.Graph()

        for vertex in self.graph.edges:
            new_graph.add_node(vertex[0])
            new_graph.add_edge(vertex[0], vertex[1])

        return new_graph

    def run(self):
        curdoc().add_root(self.layout)
        show(self.layout)
