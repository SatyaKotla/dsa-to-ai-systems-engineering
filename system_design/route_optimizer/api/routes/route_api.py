from fastapi import APIRouter, HTTPException

from system_design.route_optimizer.api.models.route_request import RouteRequest
from system_design.route_optimizer.api.models.route_response import RouteResponse
from system_design.route_optimizer.services.map_manager import map_manager
from system_design.route_optimizer.utils.logger import get_logger

loggger = get_logger(__name__)

router = APIRouter()


@router.post("/route", response_model=RouteResponse, response_model_exclude_none=True)
def compute_route(request: RouteRequest):

    loggger.info(f"API request received for map={request.map}")

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
        if result is None or not result.nodes or result.distance is None:
            raise HTTPException(
                status_code=404,
                detail="No valid route found for given start and end goal",
            )

        # Step 4: Return Response
        response = {"distance": result.distance, "path": result.nodes}
        if request.include_coordinates:
            response["coordinates"] = result.coordinates

        loggger.info("API route computed successfully")

        return response

    except ValueError as e:
        # Map validation / missing map
        loggger.error(f"Map validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

    except HTTPException as e:
        loggger.error(f"{str(e)}")
        raise e  # re-raise as-is

    except Exception as e:
        # Unexpected errors
        loggger.error(f"{str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
