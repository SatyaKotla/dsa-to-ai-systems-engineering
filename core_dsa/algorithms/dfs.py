# Depth First Search (DFS) Algorithm


# DFS using recursive method
def dfs_recursive(graph, source):
    """
    Depth First Search

    Returns:

        order: List gives order
            of the node traversal

        parent: Dict mapping nodes
            to parent node

        discovery: Dict mapping nodes
            to discovery time of the node

        finish: Dict mapping nodes
            to finish time of the node
    """
    visited = set()
    parent = {}
    order = []
    discovery = {}
    finish = {}

    time = 0

    def dfs(node):
        nonlocal time

        visited.add(node)

        time += 1
        discovery[node] = time

        order.append(node)

        for neighbor, _ in graph.neighbors(node):
            if neighbor not in visited:
                parent[neighbor] = node
                dfs(neighbor)

        time += 1
        finish[node] = time

    dfs(source)

    return {"order": order, "parent": parent, "discovery": discovery, "finish": finish}


# A helper function to reconstruct path
def reconstruct_path(parent, source, target):
    path = []
    current = target

    while current is not None:
        path.append(current)
        current = parent.get(current)

    path.reverse()

    if path[0] == source:
        return path

    return []


# DFS using iterative method


def dfs_iterative(graph, source):
    """
    Iterative Depth First Search

    Returns:
        {
            "order": traversal order,
            "parent": parent mapping,
            "discovery": discovery time,
            "finish": finish time
        }
    """

    visited = set()  # to keep track of visited nodes

    order = []
    parent = {}
    discovery = {}
    finish = {}

    time = 0  # global time counter

    stack = []  # to store (node, iterator_of_neighbors)

    # visit the source
    visited.add(source)
    parent[source] = None

    time += 1
    discovery[source] = time
    order.append(source)

    stack.append((source, iter(graph.neighbors(source))))

    while stack:
        node, neighbors = stack[-1]

        try:
            neighbor, _ = next(neighbors)

            if neighbor not in visited:

                visited.add(neighbor)
                parent[neighbor] = node

                time += 1
                discovery[neighbor] = time
                order.append(neighbor)

                stack.append((neighbor, iter(graph.neighbors(neighbor))))

        except StopIteration:

            stack.pop()

            time += 1
            finish[node] = time

    return {"order": order, "parent": parent, "discovery": discovery, "finish": finish}
