from system_design.route_optimizer.services.map_registry import MapRegistry


class MapManager:

    def __init__(self):

        self.registry = MapRegistry()

        self._register_maps()

    def _register_maps(self):

        self.registry.register_map("grid_10", "tests/data/grid_10.json", "kdtree")

        self.registry.register_map("grid_50", "tests/data/grid_50.json", "kdtree")

    def get_service(self, map_name, cost="distance"):
        return self.registry.get_service(map_name, cost)


map_manager = MapManager()
