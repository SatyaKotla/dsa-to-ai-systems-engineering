from .spatial import find_nearest_node, KDTree
from core_dsa.algorithms.astar import astar, reconstruct_path
from .route_result import RouteResult


# --------------- Router Class --------------
class Router:

    def __init__(self, graph):
        self.graph = graph
        self.kdtree = KDTree(graph)

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
            return RouteResult([], [], float("inf"))

        # Step 4: reconstruct path
        path = reconstruct_path(previous, start_node, goal_node)

        # Step 5: unreachable route check with path
        if path is None:
            return RouteResult([], [], float("inf"))

        # Step 6: get total distance
        distance = distances[goal_node]

        # Step 7 Get coordinates of the path nodes
        coordinates = [self.graph.get_coord(node) for node in path]

        return RouteResult(path, coordinates, distance)

    def _nearest_node(self, coordinates):
        # unpack coordinates
        x, y = coordinates

        return find_nearest_node(graph=self.graph, x=x, y=y, kdtree=self.kdtree)
