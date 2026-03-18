from pydantic import BaseModel


class RouteRequest(BaseModel):

    map: str
    start_lat: float
    start_lon: float
    end_lat: float
    end_lon: float
    cost: str = "distance"
