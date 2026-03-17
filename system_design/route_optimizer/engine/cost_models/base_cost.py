from abc import ABC, abstractmethod
from system_design.route_optimizer.engine.edge_metadata import EdgeMetadata


class BaseCost(ABC):
    """
    Abstract base class for routing cost models.

    A cost model converts edge metadata into a numerical
    weight that can be used by shortest-path algorithms.
    """

    @abstractmethod
    def compute(self, metadata: EdgeMetadata) -> float:
        """
        Compute the traversal cost for an edge.

        Parameters
        ----------
        metadata: EdgeMetadata
            Metadata describing the edge.

        Returns
        -------
        float
            Cost value used by routing algorithms.
        """
        pass
