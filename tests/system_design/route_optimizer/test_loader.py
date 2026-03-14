####################################################
# --------- TESTS FOR MAP LOADER COMPONENT ------- #
####################################################
from system_design.route_optimizer.loaders.map_loader import MapLoader
from pathlib import Path

DATA_DIR = Path(__file__).parents[2] / "data"

file_path = DATA_DIR / "small_map.json"


def test_map_loader():
    graph = MapLoader.from_json(file_path)

    assert "A" in graph.vertices()
    assert graph.get_coord("A") == [0, 0]
