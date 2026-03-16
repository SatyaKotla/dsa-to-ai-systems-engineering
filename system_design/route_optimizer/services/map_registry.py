from .route_service import RoutingService
from ..engine.cost_models.distance_cost import DistanceCost
from ..engine.cost_models.time_cost import TimeCost


class MapRegistry:

    def __init__(self):
        # Stores map configurations
        self._map_configs = {}

        # Cache of loaded routing services
        self._services = {}

        # Available cost models
        self.cost_models = {"distance": DistanceCost, "time": TimeCost}

    def register_map(self, name, map_path, spatial_method="kdtree"):
        """
        Register a map configuration.
        """
        self._map_configs[name] = (map_path, spatial_method)

    def load_map(self, name, cost_type="distance"):
        """
        Build and cache a routing service.
        """
        if name not in self._map_configs:
            raise ValueError(f"Map '{name}' is not registered")

        key = (name, cost_type)

        if key in self._services:
            return self._services[key]

        map_path, spatial_method = self._map_configs[name]

        if cost_type not in self.cost_models:
            raise ValueError(f"Unknown cost type '{cost_type}'")

        cost_model = self.cost_models[cost_type]()

        service = RoutingService(
            map_path=map_path, spatial_method=spatial_method, cost_model=cost_model
        )

        self._services[key] = service

        return service

    def get_service(self, name, cost_type="distance"):
        """
        Retrieve a routing service using lazy loading.
        """

        key = (name, cost_type)

        if key not in self._services:
            return self.load_map(name, cost_type=cost_type)

        return self._services[key]
