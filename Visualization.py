from bokeh.io import show
from bokeh.layouts import column, row
from bokeh.models import Dropdown, Div, Legend, LegendItem
from bokeh.plotting import from_networkx
import networkx as nx
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
from P8 import P8

#TODO
#usuwac image po kliknieciu produkcji

class Visualization:
    production_classes_by_names = {
        "Production 1": P1,
        "Production 2": P2,
        "Production 3": P3,
        "Production 4": P4,
        "Production 5": P5,
        "Production 6": P6,
        "Production 7": P7,
        "Production 8": P8,
    }
    production_selected = None
    vertices_chosen = list()
    source = None
    networkx_graph = None
    graph_renderer = None
    plot = None

    def __init__(self, graph):
        self.graph = graph
        self._create_buttons()
        self.graph_initialization()
        self.set_hover_tool_and_click_event()
        self.layout = column(self.dropdown, self.plot)
        self.layout = row(self.layout, self._create_legend())

    def _create_colors(self):
        colors = []
        labels = []
        self.source.data['index'] = list(self.graph.vertices[v].index for v in self.graph.vertices)
        for v in self.graph.vertices:
            colors.append(self.graph.vertices[v].to_color())
            labels.append(self.graph.vertices[v].label)

        self.source.data['colors'] = colors
        self.source.data['labels'] = labels

    def _create_edges_to_lists(self):
        edges_to = [[] for _ in self.graph.vertices]
        vertices_indexes = self.source.data['index']
        for edge_tuple in self.graph.edges:
            vertex_from, vertex_to = edge_tuple
            edges_to[vertices_indexes.index(vertex_from)].append(vertex_to)

        self.source.data['edges_to'] = edges_to

    def _create_buttons(self):
        self.menu = [("Production 1", "Production 1"), ("Production 2", "Production 2"),
                     ("Production 3", "Production 3"), ("Production 4", "Production 4"),
                     ("Production 5", "Production 5"), ("Production 6", "Production 6"),
                     ("Production 7", "Production 7"), ("Production 8", "Production 8")]

        self.dropdown = Dropdown(label="Productions", button_type="warning", menu=self.menu)
        self.dropdown.on_click(self._dropdown_update)

    def _create_image(self, production):
        for element in self.layout.children:
            if element.name == "production":
                self.layout.children.remove(element)

        div_image = Div(text=f"<img src='Graph-Transformations/static/images/"
                             f"{self.production_classes_by_names[production].to_string()}.jpg' width='540' height='auto'>"
                        ,name="production", margin=(5,5,5,-100))

        self.layout = row(self.layout, div_image)

        curdoc().clear()
        curdoc().add_root(self.layout)

    def _create_legend(self):
        return Div(text=f"<img src='Graph-Transformations/static/images/legend.jpg'>",margin=(200,5,5,5))

    def _dropdown_update(self, event):
        self.dropdown.label = event.item
        self._create_image(event.item)
        self.production_selected = self.production_classes_by_names.get(event.item)
        self.vertices_chosen.clear()

    def clicking_update(self, event):
        node_clicked_list = self.source.selected.indices
        if node_clicked_list and self.production_selected:
            vertex_index = list(self.networkx_graph.nodes())[node_clicked_list[0]]
            if vertex_index not in self.vertices_chosen:
                self.vertices_chosen.append(vertex_index)
            if len(self.vertices_chosen) == self.production_selected.get_vertices_number():
                self.apply_production()

    def apply_production(self):
        self.production_selected.apply([self.graph.vertices[i] for i in self.vertices_chosen], self.graph)
        self.production_selected = None
        self.vertices_chosen.clear()
        self.dropdown.label = "Productions"

        self.graph_initialization()
        self.layout.children[0] = column(self.dropdown, self.plot)

        self.set_hover_tool_and_click_event()
        curdoc().clear()
        curdoc().add_root(self.layout)

    def set_hover_tool_and_click_event(self):
        tooltips = [
            ("Index", "@index"),
            ("Edges to", "@edges_to"),
            ("Label", "@labels")
        ]
        self.plot.add_tools(HoverTool(tooltips=tooltips), TapTool(), BoxSelectTool())
        self.plot.renderers.append(self.graph_renderer)
        self.plot.select(type=TapTool)
        self.plot.on_event(Tap, self.clicking_update)

    def graph_initialization(self):
        self.networkx_graph = self._convert_graph()
        self.plot = figure(width=800, height=600, x_range=(-1.2, 1.2), y_range=(-1.2, 1.2),
                           x_axis_location=None, y_axis_location=None, toolbar_location=None,
                           title="Graph Transformations", background_fill_color="#efefef")
        self.plot.grid.grid_line_color = None
        self.graph_renderer = from_networkx(self.networkx_graph, nx.spring_layout, scale=1, center=(0, 0))
        self.source = self.graph_renderer.node_renderer.data_source
        self._create_colors()
        self._create_edges_to_lists()
        self.graph_renderer.node_renderer.glyph = Circle(size=15, fill_color="colors")
        self.graph_renderer.edge_renderer.glyph = MultiLine(line_color="black",
                                                            line_alpha=0.8, line_width=1.5)

    def _convert_graph(self):
        new_graph = nx.Graph()

        for vertex in self.graph.edges:
            new_graph.add_node(vertex[0])
            new_graph.add_edge(vertex[0], vertex[1])

        return new_graph

    def run(self):
        curdoc().add_root(self.layout)
        show(self.layout)
