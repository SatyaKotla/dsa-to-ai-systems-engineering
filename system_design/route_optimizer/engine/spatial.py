# Spatial components
import math


def find_nearest_node(graph, x, y, kdtree=None):
    """
    Finds nearest node in the graph to the given coordinates.

    Parameters
    ----------
    graph: Graph
        Graph containing nodes with coordinates
    x, y: float
        Target coordinates

    Returns
    -------
    nearest_node

    Approach: Linear Scan with an option to choose KD TREE search
    """

    if kdtree:
        return kdtree.nearest((x, y))

    # Initialize the best node
    best_node = None
    best_distance = float("inf")

    for node in graph.nodes:

        coordinates = graph.get_coord(node)

        if coordinates is None:
            continue

        nx, ny = coordinates

        dx = nx - x
        dy = ny - y

        distance = dx * dx + dy * dy  # squared distance instead of
        # square root (square root operation
        # is computationally expensive)

        if distance < best_distance:
            best_distance = distance
            best_node = node

    return best_node


############################################
# ------- KD TREE ------------------------ #
############################################


def distance(a, b):
    return math.dist(a, b)


class KDNode:
    def __init__(self, x, y, node_id, left=None, right=None):
        self.x = x
        self.y = y
        self.node_id = node_id
        self.left = left
        self.right = right


class KDTree:
    def __init__(self, graph):

        points = []

        for node in graph.vertices():
            x, y = graph.get_coord(node)
            points.append((x, y, node))

        self.root = self.build(points, depth=0)

    def build(self, points, depth):

        if not points:
            return None

        axis = depth % 2

        points.sort(key=lambda p: p[axis])

        mid = len(points) // 2

        x, y, node_id = points[mid]

        left = self.build(points[:mid], depth + 1)
        right = self.build(points[mid + 1 :], depth + 1)

        return KDNode(x, y, node_id, left, right)

    def nearest(self, target):

        best_node = None
        best_dist = float("inf")

        def search(node, depth):

            nonlocal best_node, best_dist

            if node is None:
                return

            node_point = (node.x, node.y)

            d = distance(node_point, target)

            if d < best_dist:
                best_dist = d
                best_node = node.node_id

            axis = depth % 2

            if axis == 0:
                difference = target[0] - node.x
            else:
                difference = target[1] - node.y

            if difference < 0:
                first = node.left
                second = node.right
            else:
                first = node.right
                second = node.left

            search(first, depth + 1)

            if abs(difference) < best_dist:
                search(second, depth + 1)

        search(self.root, 0)

        return best_node
