from .spatial_index import SpatialIndex
from .spatial import KDTree


class KDTreeIndex(SpatialIndex):

    def __init__(self, graph):
        self.kdtree = KDTree(graph)

    def nearest(self, x, y):
        return self.kdtree.nearest((x, y))
