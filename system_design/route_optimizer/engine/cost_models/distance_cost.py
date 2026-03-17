from system_design.route_optimizer.engine.cost_models.base_cost import BaseCost
from system_design.route_optimizer.engine.edge_metadata import EdgeMetadata


class DistanceCost(BaseCost):
    """
    Cost model that minimizes travel distance.
    """

    def compute(self, metadata: EdgeMetadata) -> float:
        return metadata.distance
