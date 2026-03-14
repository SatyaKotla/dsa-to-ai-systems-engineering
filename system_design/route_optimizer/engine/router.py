from .spatial import find_nearest_node
from core_dsa.algorithms.astar import astar, reconstruct_path


def compute_route(graph, start_coordinates, goal_coordinates):

    # unpack coordinates
    sx, sy = start_coordinates
    gx, gy = goal_coordinates

    # Step 1: find closest nodes
    start_node = find_nearest_node(graph, sx, sy)
    goal_node = find_nearest_node(graph, gx, gy)

    if start_node is None or goal_node is None:
        return None, float("inf")

    # Step 2: run A*
    distances, previous = astar(graph=graph, source=start_node, goal=goal_node)

    # Step 3: check reachability
    if distances.get(goal_node, float("inf")) == float("inf"):
        return None, float("inf")

    # Step 4: reconstruct path
    path = reconstruct_path(previous, start_node, goal_node)

    # Step 5: get total distance
    distance = distances[goal_node]

    return path, distance
