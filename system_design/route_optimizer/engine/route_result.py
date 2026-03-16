class RouteResult:

    def __init__(self, nodes, coordinates, distance, segments=None):

        self.nodes = nodes
        self.coordinates = coordinates
        self.distance = distance
        self.segments = segments or []

    def __repr__(self):
        return f"RouteResult(nodes={len(self.nodes)}, " f"distance={self.distance})"
