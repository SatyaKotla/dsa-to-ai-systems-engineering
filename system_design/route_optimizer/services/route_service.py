from system_design.route_optimizer.engine.router import Router


class RoutingService:

    def __init__(self, graph, spatial_index, snap_threshold=0.01):

        self.graph = graph

        self.index = spatial_index

        self.snap_threshold = snap_threshold

        self.router = Router(graph=self.graph, spatial_index=self.index)

        self._route_cache = {}

    def route(self, start_coordinates, goal_coordinates):

        # Validation of nodes
        self._validate_coordinates(start_coordinates)
        self._validate_coordinates(goal_coordinates)

        key = (start_coordinates, goal_coordinates)

        if key in self._route_cache:
            return self._route_cache[key]

        result = self.router.compute_route(
            start_coordinates=start_coordinates, goal_coordinates=goal_coordinates
        )

        self._route_cache[key] = result

        return result

    def _validate_coordinates(self, coordinates):
        x, y = coordinates
        _, distance = self.index.nearest_node_distance(x, y)

        if distance > self.snap_threshold:
            raise ValueError(
                f"Coordinates {coordinates} too"
                f"far from map (distance={distance:.4f})"
            )
