from .spatial_index import SpatialIndex


class BruteForceIndex(SpatialIndex):

    def __init__(self, graph):
        self.graph = graph

    def nearest(self, x, y):

        best_node = None
        best_distance = float("inf")

        for node, coordinates in self.graph.coords.items():

            dx = coordinates[0] - x
            dy = coordinates[1] - y

            distance = dx * dx + dy * dy  # squared distance insted
            # this avoid computational
            # overhead of square root

            if distance < best_distance:
                best_distance = distance
                best_node = node

        return best_node
