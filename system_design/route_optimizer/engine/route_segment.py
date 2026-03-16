class RouteSegment:

    def __init__(
        self,
        start_node,
        end_node,
        distance,
        start_coordinates,
        end_coordinates,
        metadata=None,
    ):

        self.start_node = start_node
        self.end_node = end_node
        self.distance = distance
        self.start_coordinates = start_coordinates
        self.end_coordinates = end_coordinates
        self.metadata = metadata
