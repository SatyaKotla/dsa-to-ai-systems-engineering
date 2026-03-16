from ..loaders.map_loader import MapLoader
from ..engine.router import Router
from ..engine.spatial_index_factory import create_spatial_index


class RoutingService:

    def __init__(self, map_path, spatial_method="kdtree"):

        self.graph = MapLoader.from_json(map_path)

        self.index = create_spatial_index(graph=self.graph, method=spatial_method)

        self.router = Router(graph=self.graph, spatial_index=self.index)

        self._route_cache = {}

    def route(self, start_coordinates, goal_coordinates):

        key = (start_coordinates, goal_coordinates)

        if key in self._route_cache:
            return self._route_cache[key]

        result = self.router.compute_route(
            start_coordinates=start_coordinates, goal_coordinates=goal_coordinates
        )

        self._route_cache[key] = result

        return result
