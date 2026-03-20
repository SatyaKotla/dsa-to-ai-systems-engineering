####################################################
# --------- TESTS FOR ROUTE SERVICE COMPONENT - ####
####################################################
from system_design.route_optimizer.services.route_service import RoutingService
from system_design.route_optimizer.loaders.json_loader import JSONMapLoader
from system_design.route_optimizer.engine.spatial_index_factory import (
    create_spatial_index,
)

import pytest


def test_service_route():
    loader = JSONMapLoader()
    graph = loader.load("tests/data/grid_10.json")
    spatial_index = create_spatial_index(graph=graph)

    service = RoutingService(graph=graph, spatial_index=spatial_index)

    result = service.route(start_coordinates=(0, 0), goal_coordinates=(3, 3))

    assert result.distance > 0


def test_service_route_with_invalid_coordinates():
    loader = JSONMapLoader()
    graph = loader.load("tests/data/grid_10.json")
    spatial_index = create_spatial_index(graph=graph)

    service = RoutingService(graph=graph, spatial_index=spatial_index)

    with pytest.raises(ValueError):
        service.route(start_coordinates=(1000, 1000), goal_coordinates=(2000, 2000))
