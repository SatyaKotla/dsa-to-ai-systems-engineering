import json

from system_design.route_optimizer.loaders.base_loader import BaseMapLoader
from core_dsa.graphs.adjacency_list import Graph
from system_design.route_optimizer.engine.edge_metadata import EdgeMetadata
from system_design.route_optimizer.engine.cost_models.distance_cost import DistanceCost


class JSONMapLoader(BaseMapLoader):
    """
    Loads graph from JSON file.
    """

    def __init__(self, cost_model=None):
        self.cost_model = cost_model or DistanceCost()

    def load(self, source: str):
        with open(source, "r") as f:
            data = json.load(f)

        graph = Graph(directed=True)

        # add nodes
        for node, coordinates in data["nodes"].items():
            graph.add_vertex(node, coord=coordinates)

        # add edges
        for edge in data["edges"]:

            # OLD FORMAT
            if isinstance(edge, list):
                u, v, weight = edge
                graph.add_edge(u, v, weight=weight)

            # NEW FORMAT
            elif isinstance(edge, dict):
                u = edge["from"]
                v = edge["to"]

                distance = edge.get("distance")
                speed = edge.get("speed")

                metadata = EdgeMetadata(distance=distance, speed=speed)
                weight = self.cost_model.compute(metadata)

                graph.add_edge(u, v, weight)
        return graph
