import json
from core_dsa.graphs.adjacency_list import Graph
from ..engine.edge_metadata import EdgeMetadata
from ..engine.cost_models.distance_cost import DistanceCost


class MapLoader:

    @staticmethod
    def from_json(file_path, cost_model=None):

        if cost_model is None:
            cost_model = DistanceCost()

        with open(file_path, "r") as f:
            data = json.load(f)

        graph = Graph(directed=True)

        # add nodes with coordinates
        for node, coordinates in data["nodes"].items():
            graph.add_vertex(node, coordinates)

        # add edges
        for edge in data["edges"]:

            # OLD FORMAT (grid graphs)
            if isinstance(edge, list):
                u, v, weight = edge
                graph.add_edge(u, v, weight=weight)

            # NEW FORMAT (metadata schema)
            elif isinstance(edge, dict):
                u = edge["from"]
                v = edge["to"]

                distance = edge.get("distance")
                speed = edge.get("speed")

                metadata = EdgeMetadata(distance=distance, speed=speed)

                weight = cost_model.compute(metadata)

                graph.add_edge(u, v, weight)

        return graph
