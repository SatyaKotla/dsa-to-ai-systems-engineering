from system_design.route_optimizer.loaders.map_loader import MapLoader
from system_design.route_optimizer.engine.router import Router
from system_design.route_optimizer.engine.spatial_index_factory import (
    create_spatial_index,
)


class RoutingService:

    def __init__(self, map_path, spatial_method="kdtree", cost_model=None):

        self.graph = MapLoader.from_json(file_path=map_path, cost_model=cost_model)

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
