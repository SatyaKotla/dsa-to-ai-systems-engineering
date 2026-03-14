# Spatial components


def find_nearest_node(graph, x, y):
    """
    Finds nearest node in the graph to the given coordinates.

    Parameters
    ----------
    graph: Graph
        Graph containing nodes with coordinates
    x, y: float
        Target coordinates

    Returns
    -------
    nearest_node

    Approach: Linear Scan
    """

    # Initialize the best node
    best_node = None
    best_distance = float("inf")

    for node in graph.nodes:

        coordinates = graph.get_coord(node)

        if coordinates is None:
            continue

        nx, ny = coordinates

        dx = nx - x
        dy = ny - y

        distance = dx * dx + dy * dy  # squared distance instead of
        # square root (square root operation
        # is computationally expensive)

        if distance < best_distance:
            best_distance = distance
            best_node = node

    return best_node
