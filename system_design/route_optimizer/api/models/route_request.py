from pydantic import BaseModel
from typing import Optional


class RouteRequest(BaseModel):

    map: str
    start_lat: float
    start_lon: float
    end_lat: float
    end_lon: float
    cost: str = "distance"
    include_coordinates: Optional[bool] = False  # default False
