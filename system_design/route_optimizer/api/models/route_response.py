from pydantic import BaseModel
from typing import List, Tuple, Optional


class RouteResponse(BaseModel):

    distance: float
    path: List[str]
    coordinates: Optional[List[Tuple[float, float]]] = None
