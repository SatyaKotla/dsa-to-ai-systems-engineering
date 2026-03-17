from core_dsa.algorithms.astar import astar, reconstruct_path
from system_design.route_optimizer.engine.route_result import RouteResult
from system_design.route_optimizer.engine.route_segment import RouteSegment
import math


# --------------- Router Class --------------
class Router:

    def __init__(self, graph, spatial_index, edge_metadata=None):
        self.graph = graph
        self.spatial_index = spatial_index
        self.edge_metadata = edge_metadata or {}

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

            distance = self._distance(start_coordinates, end_coordinates)

            metadata = None
            if hasattr(self, "edge_metadata"):
                metadata = self.edge_metadata.get((start, end))

            segment = RouteSegment(
                start,
                end,
                distance,
                start_coordinates,
                end_coordinates,
                metadata=metadata,
            )

            segments.append(segment)

        return segments

    def _distance(self, a, b):

        x1, y1 = a
        x2, y2 = b

        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
