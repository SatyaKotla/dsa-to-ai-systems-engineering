from system_design.route_optimizer.loaders.map_loader import MapLoader
from system_design.route_optimizer.engine.router import Router
from system_design.route_optimizer.engine.spatial_index_factory import (
    create_spatial_index,
)
from pathlib import Path

DATA_DIR = Path(__file__).parents[3] / "tests/data"
filepath = DATA_DIR / "grid_50.json"

graph = MapLoader.from_json(filepath)

index = create_spatial_index(graph=graph, method="kdtree")

router = Router(graph=graph, spatial_index=index)

start = (0, 0)
goal = (10, 10)

result = router.compute_route(start, goal)

print(f"Path nodes: {result.nodes}")
print(f"Distance: {result.distance}")
print(f"Coordinates: {result.coordinates}")
