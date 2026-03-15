# Synthetic data generation
import json


def generate_grid_graph(n, output_file):
    nodes = {}
    edges = []

    def node_id(x, y):
        return f"n{x}_{y}"

    # create nodes
    for x in range(n):
        for y in range(n):
            nodes[node_id(x, y)] = [x, y]

    # create edges
    for x in range(n):
        for y in range(n):

            if x < n - 1:
                edges.append([node_id(x, y), node_id(x + 1, y), 1])
            if y < n - 1:
                edges.append([node_id(x, y), node_id(x, y + 1), 1])

    data = {"nodes": nodes, "edges": edges}

    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    generate_grid_graph(10, "grid_10.json")
    generate_grid_graph(50, "grid_50.json")
    generate_grid_graph(100, "grid_100.json")
    generate_grid_graph(1000, "grid_1000.json")
