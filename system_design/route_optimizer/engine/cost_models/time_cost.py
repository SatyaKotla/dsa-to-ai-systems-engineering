from .base_cost import BaseCost
from ..edge_metadata import EdgeMetadata


class TimeCost(BaseCost):
    """
    Cost model that minimizes travel time.
    """

    DEFAULT_SPEED = 40.0  # km/h fallback

    def compute(self, metadata: EdgeMetadata) -> float:
        speed = metadata.speed if metadata.speed else self.DEFAULT_SPEED
        return metadata.distance / speed
