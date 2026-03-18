from pydantic import BaseModel
from typing import List, Tuple


class RouteResponse(BaseModel):

    distance: float
    path: List[str]
    coordinates: List[Tuple[float, float]]
