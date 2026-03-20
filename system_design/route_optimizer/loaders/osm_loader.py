import osmnx as ox

from system_design.route_optimizer.loaders.base_loader import BaseMapLoader
from core_dsa.graphs.adjacency_list import Graph
from system_design.route_optimizer.engine.edge_metadata import EdgeMetadata
from system_design.route_optimizer.engine.cost_models.distance_cost import DistanceCost


class OSMLoader(BaseMapLoader):

    def __init__(self, cost_model=None):
        self.cost_model = cost_model or DistanceCost()

    def load(self, source):

        # Step 1: Download graph from OSM
        G = ox.graph_from_place(source, network_type="drive")

        graph = Graph(directed=True)

        # Step 2: Add nodes
        for node_id, data in G.nodes(data=True):

            # OSMnx uses (x=lon, y=lat), convert to (lat, lon)
            lat = data.get("y")
            lon = data.get("x")

            graph.add_vertex(node_id, (lat, lon))

        for u, v, data in G.edges(data=True):

            distance = data.get("length", 1.0)

            # speed might not always exist
            speed = data.get("speed_kph", None)

            metadata = EdgeMetadata(distance=distance, speed=speed)

            weight = self.cost_model.compute(metadata=metadata)

            graph.add_edge(u, v, weight=weight)

        return graph
