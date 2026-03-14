# A STAR(*) Algorithm
from core_dsa.heap.indexed_priority_queue import IndexedPriorityQueue
import math


# Heuristic function
def euclidean_heuristic(graph, node, goal):

    coord1 = graph.get_coord(node)
    coord2 = graph.get_coord(goal)

    if coord1 is None or coord2 is None:
        return 0

    x1, y1 = coord1
    x2, y2 = coord2

    # distance to goal
    goal_distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    return goal_distance


def astar(graph, source, goal, heuristic=None):
    """
    Compute shortest path from source to goal.

    Returns:
        distances: dict mapping vertex
                                    -> shortest distance
    """
    # Check for negative edges
    if graph.negative_edge_count > 0:
        raise ValueError("A star(*) cannot handle" "negative weights")

    # Heuristic function
    if heuristic is None:
        heuristic = euclidean_heuristic

    # Initialize distances
    distances = {}

    for vertex in graph.vertices():
        distances[vertex] = float("inf")

    distances[source] = 0

    # Initializing previous to keep track of path
    previous = {v: None for v in graph.vertices()}

    # Create minimum priority queue
    priority_queue = IndexedPriorityQueue(is_min_heap=True)

    # Insert source
    priority_queue.insert(source, heuristic(graph, source, goal))

    visited = set()

    # Main loop
    while not priority_queue.is_empty():
        current, current_priority = priority_queue.pop()

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            break

        # Relax neighbors
        for neighbor, weight in graph.neighbors(current):

            new_distance = distances[current] + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current

                priority = new_distance + heuristic(graph, neighbor, goal)

                if priority_queue.contains(neighbor):
                    priority_queue.update(neighbor, priority)
                else:
                    priority_queue.insert(neighbor, priority)

    return distances, previous


# A helper function to reconstruct path
def reconstruct_path(previous, source, goal):

    if goal not in previous and goal != source:
        return None

    path = []
    current = goal

    while current is not None:
        path.append(current)

        if current == source:
            break

        current = previous.get(current)

        if current is None:
            return None

    path.reverse()
    return path


def main():
    pass


if __name__ == "__main__":
    main()
