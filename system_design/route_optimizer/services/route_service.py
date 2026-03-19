from system_design.route_optimizer.engine.router import Router


class RoutingService:

    def __init__(self, graph, spatial_index):

        self.graph = graph

        self.index = spatial_index

        self.router = Router(graph=self.graph, spatial_index=self.index)

        self._route_cache = {}

    def route(self, start_coordinates, goal_coordinates):

        key = (start_coordinates, goal_coordinates)

        if key in self._route_cache:
            return self._route_cache[key]

        result = self.router.compute_route(
            start_coordinates=start_coordinates, goal_coordinates=goal_coordinates
        )

        self._route_cache[key] = result

        return result
