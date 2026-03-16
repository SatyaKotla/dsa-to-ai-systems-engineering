####################################################
# --------- TESTS FOR MAP REGISTRY --------------- #
####################################################
from system_design.route_optimizer.services.map_registry import MapRegistry
import pytest


# Test: Map Registration
def test_register_map():

    registry = MapRegistry()

    registry.register_map("grid_10", "tests/data/grid_10.json", "kdtree")

    assert "grid_10" in registry._map_configs


# Test: Lazy loading
def test_lazy_loading():

    registry = MapRegistry()

    registry.register_map("grid_10", "tests/data/grid_10.json", "kdtree")

    # No service loaded yet
    assert len(registry._services) == 0

    registry.get_service("grid_10")

    # Service should now exist
    assert len(registry._services) == 1


# Test: Service Caching
def test_service_cache():

    registry = MapRegistry()

    registry.register_map("grid_10", "tests/data/grid_10.json", "kdtree")

    service1 = registry.get_service("grid_10")
    service2 = registry.get_service("grid_10")

    assert service1 is service2


# Test: different cost models
def test_multiple_cost_models():

    registry = MapRegistry()

    registry.register_map("grid_10", "tests/data/grid_10.json", "kdtree")

    service_distance = registry.get_service("grid_10", "distance")
    service_time = registry.get_service("grid_10", "time")

    assert service_distance is not service_time


# Test: Unknown Map
def test_unknown_map():

    registry = MapRegistry()

    with pytest.raises(ValueError):
        registry.get_service("unknown_map")


# Test: Unknown Cost Model
def test_unknown_cost():

    registry = MapRegistry()

    registry.register_map("grid_10", "tests/data/grid_10.json", "kdtree")

    with pytest.raises(ValueError):
        registry.get_service("grid_10", "invalid_cost")
