from engine.cost_models.base_cost import BaseCost
from engine.edge_metadata import EdgeMetadata


class DistanceCost(BaseCost):
    """
    Cost model that minimizes travel distance.
    """

    def compute(self, metadata: EdgeMetadata) -> float:
        return metadata.distance
