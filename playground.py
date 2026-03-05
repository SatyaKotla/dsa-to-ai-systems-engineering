# test here
from core_dsa.algorithms.dijkstra import dijkstra, reconstruct_path
from core_dsa.graphs.adjacency_list import Graph


def main():
    g = Graph(directed=True)
    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "C", 2)
    g.add_edge("C", "D", 1)

    distances, previous = dijkstra(g, "A")

    print(f"Distances: {distances}")

    path_to_d = reconstruct_path(previous=previous, target="D")
    print(f"Path from A to D: {path_to_d}")


if __name__ == "__main__":
    main()
