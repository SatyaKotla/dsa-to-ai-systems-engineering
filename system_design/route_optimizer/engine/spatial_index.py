# Spatial Index Interface


class SpatialIndex:

    def nearest(self, x, y):
        raise NotImplementedError

    def nearest_node_distance(self, x, y):
        raise NotImplementedError
