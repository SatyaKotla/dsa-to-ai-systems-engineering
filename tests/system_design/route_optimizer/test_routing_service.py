####################################################
# --------- TESTS FOR ROUTE SERVICE COMPONENT - ####
####################################################
from system_design.route_optimizer.services.route_service import RoutingService


def test_service_route():

    service = RoutingService(map_path="tests/data/grid_10.json")

    result = service.route(start_coordinates=(0, 0), goal_coordinates=(3, 3))

    assert result.distance > 0
