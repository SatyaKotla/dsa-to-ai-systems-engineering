# Dijkstra's Algorithm
from core_dsa.heap.indexed_priority_queue import IndexedPriorityQueue
from core_dsa.graphs.adjacency_list import Graph


def dijkstra(graph, source):
    """
    Compute shortest path distances from source to all
    vertices.

    Returns:
        distances: dict mapping vertex 
                                    -> shortest distance  
    """
    
    # Initialize distances
    distances = {}
    
    for vertex in graph.vertices():
        distances[vertex] = float("inf")
    
    distances[source] = 0

    # Initializing previous to keep track of path
    previous = {v: None for v in graph.vertices()}

    # Create minimum priority queue
    priority_queue = IndexedPriorityQueue(
                is_min_heap=True)
    
    # Insert source
    priority_queue.insert(source, 0)

    # Main loop
    while not priority_queue.is_empty():
        current, current_distance = priority_queue.pop()

        # Relax neighbors
        for neighbor, weight in graph.neighbors(current):

            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current

                if priority_queue.contains(neighbor):
                    priority_queue.update(neighbor, 
                                          new_distance)
                else:
                    priority_queue.insert(neighbor,
                                          new_distance)
    
    return distances, previous

# A helper function to reconstruct path
def reconstruct_path(previous, target):
    path = []
    current = target

    while current is not None:
        path.append(current)
        current = previous[current]
    
    path.reverse()
    return path 

def main():
    pass

if __name__ == "__main__":
    main()



    