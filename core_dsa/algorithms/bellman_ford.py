# ------------------------------
# BELLMAN-FORD ALGORITHM
# ------------------------------


def bellman_ford(graph, source):
    """
    Computes shortest path from source to all vertices
    using Bellman-Ford

    Args:
        graph: list of edges(u, v, weight)\
        soruce: starting vertex

    Returns:
        distance: dict containing shortest distances
        parent: dict for path reconstruction

    Raises:
        ValueError: if a negative weight cycle exists
    """

    # Step 1: initialize weights
    distances = {v: float("inf") for v in graph.vertices()}
    distances[source] = 0

    # Initialize previous to keep track of path
    previous = {v: None for v in graph.vertices()}

    # Step 2: relaxa edge weights V-1 times
    for _ in range(len(graph.vertices()) - 1):
        for u, v, w in graph.edges():
            if distances[u] != float("inf") and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                previous[v] = u

    # Step 3: detect negative cycle
    for u, v, w in graph.edges():
        if distances[u] != float("inf") and distances[u] + w < distances[v]:
            raise ValueError("Graph contains a " "negative weight cycle")

    return distances, previous


# A helper function to reconstruct path
def reconstruct_path(previous, target):
    path = []
    current = target

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path
