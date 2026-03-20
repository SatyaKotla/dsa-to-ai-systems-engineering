from system_design.route_optimizer.services.route_service import RoutingService
from system_design.route_optimizer.engine.cost_models.distance_cost import DistanceCost
from system_design.route_optimizer.engine.cost_models.time_cost import TimeCost
from system_design.route_optimizer.engine.spatial_index_factory import (
    create_spatial_index,
)
from system_design.route_optimizer.utils.logger import get_logger

logger = get_logger(__name__)


class MapRegistry:

    def __init__(self):
        # Stores map configurations
        self._map_configs = {}

        # Cache of loaded routing services
        self._services = {}

        # Available cost models
        self.cost_models = {"distance": DistanceCost, "time": TimeCost}

        # Loader registry
        self._loaders = {}

    def register_loader(self, name, loader):
        """
        Register a map loader(e.g., 'json', 'osm')
        """
        self._loaders[name] = loader

    def register_map(
        self,
        name,
        map_path,
        spatial_method="kdtree",
        loader_type="json",
        snap_threshold=0.01,
    ):
        """
        Register a map configuration.
        """
        self._map_configs[name] = (
            map_path,
            spatial_method,
            loader_type,
            snap_threshold,
        )

    def load_map(self, name, cost_type="distance"):
        """
        Build and cache a routing service.
        """
        logger.info(f"Loading map: {name} with cost={cost_type}")

        if name not in self._map_configs:
            raise ValueError(f"Map '{name}' is not registered")

        key = (name, cost_type)

        if key in self._services:
            return self._services[key]

        map_path, spatial_method, loader_type, snap_threshold = self._map_configs[name]

        if cost_type not in self.cost_models:
            raise ValueError(f"Unknown cost type '{cost_type}'")

        cost_model = self.cost_models[cost_type]()

        # New: Load graph
        if loader_type not in self._loaders:
            raise ValueError(f"Loader '{loader_type}' not registered")

        base_loader = self._loaders[loader_type]

        # Inject cost model into loader
        loader = base_loader(cost_model=cost_model)
        graph = loader.load(map_path)

        # New: Build spatial index here
        spatial_index = create_spatial_index(graph=graph, method=spatial_method)

        # New: Pass ready objects
        service = RoutingService(
            graph=graph, spatial_index=spatial_index, snap_threshold=snap_threshold
        )

        logger.info(f"Map loaded and service created: {name}")

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
