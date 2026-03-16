from .route_service import RoutingService


class MapRegistry:

    def __init__(self):

        self._services = {}

    def load_map(self, name, map_path, spatial_method="kdtree"):

        service = RoutingService(map_path=map_path, spatial_method=spatial_method)

        self._services[name] = service

    def get_service(self, name):

        if name not in self._services:
            raise ValueError(f"Map '{name}' not loaded")

        return self._services[name]
