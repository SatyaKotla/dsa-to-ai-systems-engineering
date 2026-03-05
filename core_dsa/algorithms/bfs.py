# Breadth First Search (BFS) Algorithm

from collections import deque


def bfs(graph, source, target=None):
    """
    Breadth First Search

    Returns:
        distance: dict mapping nodes
            to shortest distance from source

        parent: dict mapping nodes
            to parent node
    """

    visited = set([source])
    queue = deque([source])

    distances = {source: 0}
    parent = {}

    while queue:
        node = queue.popleft()

        if node == target:
            break

        for neighbor, _ in graph.neighbors(node):

            if neighbor not in visited:
                visited.add(neighbor)

                parent[neighbor] = node
                distances[neighbor] = distances[node] + 1

                queue.append(neighbor)

    return distances, parent


# Path reconstruction
def reconstruct_path(parent, source, target):

    path = []
    node = target

    while node != source:
        path.append(node)
        node = parent[node]

    path.append(source)

    return path[::-1]
