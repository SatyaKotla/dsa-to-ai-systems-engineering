####################################################
# --------- TESTS FOR ROUTE OPTMIZER API ------- ###
####################################################
from fastapi.testclient import TestClient
from system_design.route_optimizer.api.main import app
import os

API_KEY = os.getenv("API_KEY", "dev-secret-key")

client = TestClient(app)


# Test: Happy path (basic route)
def test_route_success():
    response = client.post(
        "/route",
        json={
            "map": "grid_10",
            "start_lat": "0",
            "start_lon": "0",
            "end_lat": "9",
            "end_lon": "9",
            "include_coordinates": False,
        },
        headers={"x-api-key": API_KEY},
    )

    assert response.status_code == 200

    data = response.json()

    assert "path" in data
    assert "distance" in data
    assert "coordinates" not in data


# Test: With coordinates
def test_route_with_coordinates():
    response = client.post(
        "/route",
        json={
            "map": "grid_10",
            "start_lat": "0",
            "start_lon": "0",
            "end_lat": "9",
            "end_lon": "9",
            "include_coordinates": True,
        },
        headers={"x-api-key": API_KEY},
    )

    assert response.status_code == 200

    data = response.json()

    assert "coordinates" in data
    assert isinstance(data["coordinates"], list)


# Test: Same start and end coodinates
def test_route_same_start_end():
    response = client.post(
        "/route",
        json={
            "map": "grid_10",
            "start_lat": "0",
            "start_lon": "0",
            "end_lat": "0",
            "end_lon": "0",
            "include_coordinates": True,
        },
        headers={"x-api-key": API_KEY},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["distance"] == 0
    assert data["coordinates"] == [[0, 0]]


# Test: Invalid node
def test_route_invalid_input():
    response = client.post(
        "/route",
        json={
            "map": "grid_10",
            "start_lat": "0",
            "start_lon": "0",
            "end_lat": "1",
            "end_lon": "b",
            "include_coordinates": False,
        },
        headers={"x-api-key": API_KEY},
    )

    assert response.status_code == 422

    data = response.json()
    assert "detail" in data


# Test: Invalid map
def test_route_invalid_map():
    response = client.post(
        "/route",
        json={
            "map": "unknown_map",
            "start_lat": "0",
            "start_lon": "0",
            "end_lat": "5",
            "end_lon": "5",
            "include_coordinates": False,
        },
        headers={"x-api-key": API_KEY},
    )

    assert response.status_code == 400


# Test: Route out of bounds
def test_route_out_of_bounds_coordinates():
    response = client.post(
        "/route",
        json={
            "map": "grid_10",
            "start_lat": "100",
            "start_lon": "100",
            "end_lat": "200",
            "end_lon": "200",
            "include_coordinates": False,
        },
        headers={"x-api-key": API_KEY},
    )

    assert response.status_code == 400

    data = response.json()
    assert "too far" in data["detail"]
