# Prim's Algorithm
from core_dsa.heap.indexed_priority_queue import IndexedPriorityQueue


def prim(graph, source):

    mst = []
    total_weight = 0

    priority_queue = IndexedPriorityQueue(is_min_heap=True)
    weights = {}
    parent = {}

    for v in graph.vertices():
        weights[v] = float("inf")
        priority_queue.insert(v, float("inf"))

    # insert source
    weights[source] = 0
    priority_queue.update(source, 0)

    while not priority_queue.is_empty():

        current, current_weight = priority_queue.pop()

        if current in parent:
            mst.append((parent[current], current, current_weight))
            total_weight += current_weight

        for neighbor, weight in graph.neighbors(current):

            if priority_queue.contains(neighbor) and weight < weights[neighbor]:

                weights[neighbor] = weight
                parent[neighbor] = current
                priority_queue.update(neighbor, weight)

    return mst, total_weight
