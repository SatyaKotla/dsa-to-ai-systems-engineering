from core_dsa.algorithms.dfs import dfs_iterative


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
