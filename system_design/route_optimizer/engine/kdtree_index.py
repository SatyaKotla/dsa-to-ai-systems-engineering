from system_design.route_optimizer.engine.spatial_index import SpatialIndex
from system_design.route_optimizer.engine.spatial import KDTree


class KDTreeIndex(SpatialIndex):

    def __init__(self, graph):
        self.kdtree = KDTree(graph)

    def nearest(self, x, y):
        return self.kdtree.nearest((x, y))
