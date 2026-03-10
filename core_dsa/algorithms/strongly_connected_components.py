# STRONGLY CONNECTED COMPONENTS (SCC)

# ------------------------------------------
# Kosaraju's algorithm
# ------------------------------------------


def scc_kosaraju(graph):
    """
    Compute Strongly Connected Components (SCC) in a
    directed graph using Kosaraju's Algorithm.

    Args:
        graph (dict): Directed graph

    Returns:
        list[list]: List of strongly connected components
    """

    visited = set()
    stack = []

    # Step 1: DFS to get finish order
    def dfs(node):
        visited.add(node)

        for neighbor, _ in graph.neighbors(node):
            if neighbor not in visited:
                dfs(neighbor)

        stack.append(node)

    for node in graph.vertices():
        if node not in visited:
            dfs(node)

    # Step 2: Reverse graph
    reversed_graph = {node: [] for node in graph.vertices()}

    for node in graph.vertices():
        for neighbor, _ in graph.neighbors(node):
            reversed_graph[neighbor].append(node)

    # Step 3: DFS using finish order
    visited.clear()
    scc_list = []

    def dfs_reverse(node, component):
        visited.add(node)
        component.append(node)

        for neighbor in reversed_graph[node]:
            if neighbor not in visited:
                dfs_reverse(neighbor, component)

    while stack:
        node = stack.pop()

        if node not in visited:
            component = []
            dfs_reverse(node, component)
            scc_list.append((component))

    return scc_list
