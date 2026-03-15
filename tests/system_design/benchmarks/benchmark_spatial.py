import time
import random
from system_design.route_optimizer.engine.spatial import find_nearest_node, KDTree
from system_design.route_optimizer.loaders.map_loader import MapLoader


def benchmark(dataset_path, num_queries=100):

    graph = MapLoader.from_json(dataset_path)

    num_nodes = len(graph.nodes)

    # Build time list
    brute_times = []
    kd_times = []

    # Build the KDTree outside the loop
    my_kdtree = KDTree(graph)

    for _ in range(num_queries):

        x = random.uniform(0, 100)
        y = random.uniform(0, 100)

        # ----------------brute force (Linear Scan)-------------
        brute_start_time = time.perf_counter()

        _ = find_nearest_node(graph=graph, x=x, y=y, kdtree=None)

        brute_times.append(time.perf_counter() - brute_start_time)

        # ------------------ KD Tree (system benchmark) ---------------------------
        kd_start_time = time.perf_counter()

        _ = find_nearest_node(graph=graph, x=x, y=y, kdtree=my_kdtree)

        kd_times.append(time.perf_counter() - kd_start_time)

    brute_avg_time = sum(brute_times) / len(brute_times)
    kd_avg_time = sum(kd_times) / len(kd_times)

    return num_nodes, brute_avg_time, kd_avg_time


def main():

    datasets = [
        "tests/data/grid_10.json",
        "tests/data/grid_50.json",
        "tests/data/grid_100.json",
        "tests/data/grid_1000.json",
    ]

    print("\nSpatial Search Benchmark\n")

    for dataset in datasets:

        num_nodes, brute, kd = benchmark(dataset_path=dataset)

        print(f"{dataset}")
        print(f"Nodes: {num_nodes}")
        print(f"Brute Force Average: {brute:.8f} sec")
        print(f"KD Tree Avg: {kd:.8f} sec")
        if kd > 0:
            print(f"Speedup: {brute/kd:.2f}x")
        print("=" * 40)


if __name__ == "__main__":
    main()
