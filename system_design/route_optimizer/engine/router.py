from core_dsa.algorithms.astar import astar, reconstruct_path
from .route_result import RouteResult
from .route_segment import RouteSegment


# --------------- Router Class --------------
class Router:

    def __init__(self, graph, spatial_index):
        self.graph = graph
        self.spatial_index = spatial_index

    def compute_route(self, start_coordinates, goal_coordinates):

        # Step 1: find closest nodes
        start_node = self._nearest_node(start_coordinates)

        goal_node = self._nearest_node(goal_coordinates)

        if start_node is None or goal_node is None:
            return None, float("inf")

        # Step 2: run A*
        distances, previous = astar(graph=self.graph, source=start_node, goal=goal_node)

        # Step 3: check reachability
        if distances.get(goal_node, float("inf")) == float("inf"):
            return RouteResult([], [], float("inf"), [])

        # Step 4: reconstruct path
        path = reconstruct_path(previous, start_node, goal_node)

        # Step 5: unreachable route check with path
        if path is None:
            return RouteResult([], [], float("inf"), [])

        # Step 6: get total distance
        distance = distances[goal_node]

        # Step 7: Get coordinates of the path nodes
        coordinates = [self.graph.get_coord(node) for node in path]

        # Step 8: Convert nodes into segments
        segments = self._build_segments(nodes=path)

        return RouteResult(path, coordinates, distance, segments)

    def _nearest_node(self, coordinates):
        # unpack coordinates
        x, y = coordinates

        return self.spatial_index.nearest(x, y)

    def _build_segments(self, nodes):

        segments = []

        for i in range(len(nodes) - 1):

            start = nodes[i]
            end = nodes[i + 1]

            start_coordinates = self.graph.coords[start]
            end_coordinates = self.graph.coords[end]

            dx = end_coordinates[0] - start_coordinates[0]
            dy = end_coordinates[1] - start_coordinates[1]

            distance = (dx * dx + dy * dy) ** 0.5

            segment = RouteSegment(
                start, end, distance, [start_coordinates, end_coordinates]
            )

            segments.append(segment)

        return segments
