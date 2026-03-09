# CYCLE DETECTION

# ------------------------------
# Directed Graph Cycle Detection
# ------------------------------


def detect_cycle_directed(graph):
    """
    Detect cycle in a directed graph using DFS.

    Parameters
    ----------
    graph: Graph
        Graph object with neighbors(node) method.

    Returns:
        bool
            True if cycle exits, False otherwise
    """
    visited = set()
    recursion_stack = set()

    def dfs(node):
        visited.add(node)
        recursion_stack.add(node)

        for neighbor, _ in graph.neighbors(node):

            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in recursion_stack:
                return True

        recursion_stack.remove(node)
        return False

    for node in graph.vertices():
        if node not in visited:
            if dfs(node):
                return True
    return False


# ------------------------------
# Undirected Graph Cycle Detection
# ------------------------------


def detect_cycle_undirected(graph):
    """
    Detect cycle in a undirected graph using DFS.

    Parameters
    ----------
    graph: Graph
        Graph object with neighbors(node) method.

    Returns:
        bool
            True if cycle exits, False otherwise
    """
    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor, _ in graph.neighbors(node):

            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True

        return False

    for node in graph.vertices():
        if node not in visited:
            if dfs(node, None):
                return True
    return False
