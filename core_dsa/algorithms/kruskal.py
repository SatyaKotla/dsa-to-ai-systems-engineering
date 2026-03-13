# Kruskal Algorithm
from core_dsa.graphs.disjoint_set import DijointSet


def kruskal(vertices, edges):

    # Step 1: Initialize disjoint set
    ds = DijointSet()

    for v in vertices:
        ds.make_set(v)

    # Step 2: Sort edges by weight
    edges = sorted(edges, key=lambda x: x[2])

    mst = []
    total_weight = 0

    # Step 3: Process edges
    for u, v, weight in edges:

        # Step 4: Check if cycle will form
        if ds.find(u) != ds.find(v):

            ds.union(u, v)

            mst.append((u, v, weight))
            total_weight += weight

            # Break the cycle if loop is equals v - 1
            if len(mst) == len(vertices) - 1:
                break
    return mst, total_weight
