from .route_service import RoutingService


class MapRegistry:

    def __init__(self):

        self._services = {}
        self._map_configs = {}

    def register_map(self, name, map_path, spatial_method="kdtree"):
        self._map_configs[name] = (map_path, spatial_method)

    def load_map(self, name, map_path, spatial_method="kdtree"):

        service = RoutingService(map_path=map_path, spatial_method=spatial_method)

        self._services[name] = service

    def get_service(self, name):

        if name not in self._services:

            if name not in self._map_configs:
                raise ValueError(f"Map '{name}' not loaded")

            map_path, spatial_method = self._map_configs[name]

            service = RoutingService(map_path=map_path, spatial_method=spatial_method)

            self._services[name] = service

        return self._services[name]
