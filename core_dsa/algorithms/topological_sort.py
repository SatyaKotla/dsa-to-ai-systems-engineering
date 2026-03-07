from core_dsa.algorithms.dfs import dfs_iterative


# simple topological sort
def topological_sort(graph):
    """
    Perform topological sort on a directed acylic graph (DAG).

    Returns nodes ordered by dependency.

    Raises: Value Error if the graph is undirected.
    """
    if not graph._directed:
        raise ValueError(
            """Topological sort requires
                         a directed graph."""
        )

    result = dfs_iterative(graph)

    finish_time = result["finish"]

    # sort nodes by decreasing finish time
    topo_order = sorted(finish_time, key=lambda node: finish_time[node], reverse=True)

    return topo_order
