import json
from core_dsa.graphs.adjacency_list import Graph


class MapLoader:

    @staticmethod
    def from_json(file_path):

        with open(file_path, "r") as f:
            data = json.load(f)

        graph = Graph(directed=True)

        # add nodes with coordinates
        for node, coordinates in data["nodes"].items():
            graph.add_vertex(node, coordinates)

        # add edges
        for source, target, weight in data["edges"]:
            graph.add_edge(source, target, weight)

        return graph
