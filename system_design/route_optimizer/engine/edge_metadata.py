from dataclasses import dataclass
from typing import Optional


@dataclass
class EdgeMetadata:
    """
    Stores metadata associated with a road segment (edge).
    This class only stores data. Cost models decide how to
    compute the routing weight using this metadata.
    """

    distance: float
    speed: Optional[float] = None
    road_type: Optional[str] = None
