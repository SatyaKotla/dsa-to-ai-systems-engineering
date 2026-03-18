from fastapi import APIRouter, HTTPException

from system_design.route_optimizer.api.models.route_request import RouteRequest
from system_design.route_optimizer.api.models.route_response import RouteResponse
from system_design.route_optimizer.services.map_manager import map_manager

router = APIRouter()


@router.post("/route", response_model=RouteResponse)
def compute_route(request: RouteRequest):

    try:
        # Step 1: Convert input to internal format
        start = (request.start_lat, request.start_lon)
        end = (request.end_lat, request.end_lon)

        # Step 2: Call MapManager
        service = map_manager.get_service(request.map, request.cost)

        if not service:
            raise HTTPException(status_code=404, detail="Map not found")

        result = service.route(start, end)

        # Step 3: Handle no route
        if result is None or result.nodes is None:
            raise HTTPException(status_code=404, detail="Route not found")

        # Step 4: Return Response
        return RouteResponse(
            distance=result.distance, path=result.nodes, coordinates=result.coordinates
        )

    except ValueError as e:
        # Map validation / missing map
        raise HTTPException(status_code=400, detail=str(e))

    except Exception:
        # Unexpected errors
        raise HTTPException(status_code=500, detail="Internal server error")
