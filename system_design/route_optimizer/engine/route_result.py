class RouteResult:

    def __init__(self, nodes, coordinates, distance):

        self.nodes = nodes
        self.coordinates = coordinates
        self.distance = distance

    def __repr__(self):
        return f"RouteResult(nodes={len(self.nodes)}, " f"distance={self.distance})"
