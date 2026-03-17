from system_design.route_optimizer.engine.kdtree_index import KDTreeIndex
from system_design.route_optimizer.engine.brute_force_index import BruteForceIndex


def create_spatial_index(graph, method="kdtree"):
    """
    Create spatial index.

    Supported methods:
    - "kdtree"
    - "bruteforce"
    """

    if method == "kdtree":
        return KDTreeIndex(graph)

    if method == "bruteforce":
        return BruteForceIndex(graph)

    raise ValueError(f"Unknown spatial index method: {method}")
