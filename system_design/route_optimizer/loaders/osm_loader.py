import osmnx as ox

from system_design.route_optimizer.loaders.base_loader import BaseMapLoader
from core_dsa.graphs.adjacency_list import Graph
from system_design.route_optimizer.engine.edge_metadata import EdgeMetadata
from system_design.route_optimizer.engine.cost_models.distance_cost import DistanceCost
from pathlib import Path


class OSMLoader(BaseMapLoader):

    def __init__(self, cost_model=None):
        self.cost_model = cost_model or DistanceCost()

    def load(self, source):

        # Step 1: Load graph from OSM

        # -----------------------------
        # Configure OSMnx HTTP cache
        # -----------------------------
        http_cache_dir = Path(__file__).parent.parent / "data" / "osm_http_cache"
        http_cache_dir.mkdir(parents=True, exist_ok=True)

        ox.settings.cache_folder = str(http_cache_dir)
        ox.settings.use_cache = True

        # -----------------------------
        # Setup Graph Cache
        # -----------------------------
        graph_cache_dir = Path(__file__).parent.parent / "data" / "osm_cache"
        graph_cache_dir.mkdir(parents=True, exist_ok=True)

        # create file name
        file_name = source.replace(" ", "_").replace(",", "") + ".graphml"
        graph_cache_path = graph_cache_dir / file_name

        # -----------------------------
        # Load or Download Graph
        # -----------------------------
        if graph_cache_path.exists():
            print("Loading graph from cache...")
            G = ox.load_graphml(graph_cache_path)
        else:
            print("Downloading graph from OSM")
            G = ox.graph_from_place(source, network_type="drive")
            ox.save_graphml(G, graph_cache_path)

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
