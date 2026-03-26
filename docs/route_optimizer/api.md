# 🔌 API Specification

## 📌 Overview

This document defines the API interface for the Route Optimization and Navigation System.

The API enables clients(e.g., frontend applications) to request optimal routes between two points on a selected map.

---

## 🌐 Base URL

`http://127.0.0.1:8000`

---

## 📍 Endpoint: Compute Route

### 🔹 POST `/route`

Computes the optimal route between a start and end location.

## 📥 Request Format

### 🔸 Headers

Content-Type: application/json

### 🔸 Request Body

    {
        "map": "grid_10",
        "start_lat": 0,
        "start_lon": 0,
        "end_lat": 5,
        "end_lon": 5,
        "cost": "distance",
        "include_coordinates": true
    }

### 🔹 Field Definitions

| Field  |      Type    |  Required | Description |
|:----------|:-------------|:------:|:------|
| map |  string | ✅ | Map identifier (e.g., grid_10, grid_50, osm_nyc) |
|start_lat|    float  |   ✅ |Start latitude |
|start_lon| float |    ✅ |Start longitude |
|end_lat |    float |✅ |Destination latitude |
|end_lon | float |    ✅ |Destination longitude |
|cost | string |    ❌ |Cost metric (default: distance) |
|include_coordinates | boolean |   ❌ |Include route coordinates in response |

---

## 📤 Response Format

### 🔸 Success Response
    {
        "distance": 1510.02,
        "path": ["n0_0", "n0_1", "n1_1", ...],
        "coordinates":
        [
            [0, 0],
            [0, 1],
            [1, 1],  ...
        ]
    }

### 🔹 Field Definitions

| Field  |      Type    | Description |
|:----------|:-------------|:------|
| distance |  float  | Total route cost |
|path|    list[string]  |Sequence of node IDs |
|coordinates| list[list[float]] |Optional list of (lat, lon) pairs |

---

## ⚠️ Error Handling

### 🔸 Example Error Response

    {
        "detail": "No valid path found between selected nodes"
    }

### 🔹 Common Errors

| Scenario  | Description |
|:----------|:------|
| Invalid map | Map not registered in the system |
| Invalid coordinates | Coordinates too far from valid nodes |
| No path found | Graph is disconnected |
| Missing fields | Invalid request format |\

---

## 🧭 Supported Maps

Examples:

    grid_10
    grid_50
    osm_nyc

👉 Available maps depend on configuration.

---

## 🧪 Example Request (curl)

    curl -x POST "http://127.0.0.1:8000/route"\
    -H "Content-Type: application/json" \
    -d '{
            "map": "grid_10",
            "start_lat": 0,
            "start_lon": 0,
            "end_lat": 5,
            "end_lon": 5,
            "cost": "distance",
            "include_coordinates": true
    }'

---

## 📄 Notes

- Grid maps require coordinates aligned with valid nodes (snapping handled in frontend)
- OSM maps require nearest-node matching
- API is stateless

---

## ⏩ Future Enhancements

- Multiple route options
- Additional cost metrics
- Batch route computation
- Authentication and rate limiting

---

## 💡 Key Insights

- Simple and consistent interface
- Supports mutliple map types
- Decoupled from frontend implementation
- Designed for extensibility
