from core_dsa.algorithms.dfs import dfs_iterative
from collections import deque


# simple topological sort
def topological_sort(graph):
    """
    Perform topological sort on a directed acylic graph (DAG).

    Returns nodes ordered by dependency.

    Raises: Value Error if the graph is undirected.
    """
    if not graph._directed:
        raise ValueError("Topological sort requires " "a directed graph.")

    result = dfs_iterative(graph)

    finish_time = result["finish"]

    # sort nodes by decreasing finish time
    topo_order = sorted(finish_time, key=lambda node: finish_time[node], reverse=True)

    return topo_order


# topological sort using stack and cycle detection
def topological_sort_stack(graph):
    """
    Peform topological sort using stack to improve
    the performance over sorting of dfs finish times.

    Return nodes ordered by dependecy.

    Raises: value error if the graph contains cycles.
    """

    visited = set()
    recursion_stack = set()
    stack = []

    def dfs(node):

        visited.add(node)
        recursion_stack.add(node)

        for neighbor in graph.neighbors(node):

            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in recursion_stack:
                return True

        recursion_stack.remove(node)
        stack.append(node)

    for node in graph.vertices():
        if node not in visited:
            if dfs(node):
                raise ValueError("Graph contains cycle")

    return stack[::-1]


# ----------------------------
# KAHN'S ALGORITHM
# ----------------------------


def topological_sort_kahn(graph):
    """
    Perform topological sort using Kahn's algorithm.

    Args:
        graph: Graph object (directed)

    Returns:
        list: topological ordering of vertices

    Raises:
        ValueError: if graph contains a cycle
    """

    # Step1: compute in-degrees (incoming edges
    # at the node)
    in_degree = {v: 0 for v in graph.vertices()}

    for u in graph.vertices():
        for v, _ in graph.neighbors(u):
            in_degree[v] += 1

    # Step2: queue of zero in-degree nodes
    queue = deque([v for v in graph.vertices() if in_degree[v] == 0])

    topo_order = []

    # Step3: process nodes
    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor, _ in graph.neighbors(node):
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: cycle detection
    if len(topo_order) != len(graph.vertices()):
        raise ValueError("Graph contains a cycle")

    return topo_order
