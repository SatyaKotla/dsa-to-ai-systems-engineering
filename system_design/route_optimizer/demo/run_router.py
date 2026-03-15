from system_design.route_optimizer.loaders.map_loader import MapLoader
from system_design.route_optimizer.engine.router import Router
from pathlib import Path

DATA_DIR = Path(__file__).parents[3] / "tests/data"
filepath = DATA_DIR / "grid_50.json"

graph = MapLoader.from_json(filepath)

router = Router(graph)

start = (0, 0)
goal = (10, 10)

path, distance = router.compute_route(start, goal)

print(f"Router: {path}")
print(f"Distance: {distance}")
