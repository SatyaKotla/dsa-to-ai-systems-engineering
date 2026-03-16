####################################################
# --------- TESTS FOR ROUTING INTEGRATION -------- #
####################################################
from system_design.route_optimizer.loaders.map_loader import MapLoader
from system_design.route_optimizer.engine.router import Router
from system_design.route_optimizer.engine.spatial_index_factory import (
    create_spatial_index,
)
from pathlib import Path

DATA_DIR = Path(__file__).parents[2] / "data"

file_path = DATA_DIR / "grid_10.json"


def test_route_from_json():

    graph = MapLoader.from_json(file_path)

    index = create_spatial_index(graph=graph, method="kdtree")

    router = Router(graph=graph, spatial_index=index)

    start = (0, 0)
    goal = (4, 4)

    result = router.compute_route(start, goal)

    assert result.nodes is not None
    assert result.distance >= 0
