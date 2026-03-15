import time

from system_design.route_optimizer.loaders.map_loader import MapLoader
from system_design.route_optimizer.engine.spatial import find_nearest_node


def benchmark(file_path, x, y):

    graph = MapLoader.from_json(file_path=file_path)

    start = time.time()

    node = find_nearest_node(graph=graph, x=x, y=y)

    end = time.time()

    print(f"Dataset: {file_path}")
    print(f"Nearest node: {node}")
    print(f"Time: {end-start:.6f} seconds")
    print("-" * 40)


if __name__ == "__main__":
    benchmark("tests/data/grid_10.json", 5.2, 4.1)
    benchmark("tests/data/grid_50.json", 20.3, 10.4)
    benchmark("tests/data/grid_100.json", 59.7, 60.2)
    benchmark("tests/data/grid_1000.json", 500.1, 700.3)
