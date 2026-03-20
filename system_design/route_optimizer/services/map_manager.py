from system_design.route_optimizer.services.map_registry import MapRegistry
from system_design.route_optimizer.loaders.json_loader import JSONMapLoader
from system_design.route_optimizer.loaders.osm_loader import OSMLoader
import json
from pathlib import Path


class MapManager:

    def __init__(self):

        self.registry = MapRegistry()

        # Register loaders
        self.registry.register_loader("json", JSONMapLoader)
        self.registry.register_loader("osm", OSMLoader)

        self._register_maps()

    def _register_maps(self):

        config_path = Path(__file__).parent.parent / "config" / "maps.json"

        with open(config_path, "r") as f:
            config = json.load(f)

        for map_name, map_config in config["maps"].items():

            self.registry.register_map(
                name=map_name,
                map_path=map_config["source"],
                spatial_method=map_config.get("spatial", "kdtree"),
                loader_type=map_config.get("loader", "json"),
                snap_threshold=map_config.get("snap_threshold", 0.01),
            )

    def get_service(self, map_name, cost="distance"):
        return self.registry.get_service(map_name, cost)


map_manager = MapManager()
