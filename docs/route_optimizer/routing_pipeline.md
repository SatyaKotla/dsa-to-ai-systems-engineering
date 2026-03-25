# 🔄 Routing Pipeline
## 📌 Overview

This document describes the end-to-end execution flow of a route request, from user interaction in the frontend to path computation in the backend and final visualization.

The pipeline demonstrates how different layers of the system collaborates to compute and return the optimal route.

---
## 🧭 High Level Overview

    User Interaction (Frontend)
            ↓
    API Request (FastAPI)
            ↓
    Map Manager (Service Layer)
            ↓
    Map Registry (Graph Access)
            ↓
    Routing Service (Business Logic)
            ↓
    A* Algorithm (Engine)
            ↓
    Response (Path + Coordinates)
            ↓
    Frontend Visualization

---
## 🔄 Step-by-Step Execution

1️⃣ User Interaction (Frontend)

- User clicks on the map to select:
    - Start location
    - Destination
- Frontend captures:
    - Latitude, and longitude
    - Selected map (e.g., grid or OSM)
- For grid maps:
    - Coordinates are snapped to nearest valid node

2️⃣ API Request

- Frontend sends a POST request to:
    /route
- Request payload includes:

        {
            "map": "grid_10",
            "start_lat": 0,
            "start_lon": 0,
            "end_lat": 5,
            "end_lon": 5,
            "cost": "distance",
            "include_coordinates": true
        }

3️⃣ API Layer Processing

- FastAPI endpoint:
    - Validates request schema
    - Extracts parameters
    - Forwards request to service layer

4️⃣ Map Manager (Service Layer)

- Determines which map is requested
- Requests graph data from Map Registry
- Ensures correct loader is used (OSM or grid)

5️⃣ Map Registry (Infrastructure Layer)

- Checks if graph is already loaded (cache)
- If not:
    - Loads graph using appropriate loader
- Returns graph object to Map Manager

6️⃣ Routing Service (Domain Logic)

- Receives:
    - Graph
    - Start Node
    - End Node
- Prepares input for routing engine
- Calls Router

7️⃣ Router (A* Algorithm Execution)

- Calls A* Algorithm
- Computes route
- A* Algorithm
    - Performs path finding:
        - Heuristic-based search
        - Cost accumulation
- Outputs:
    - Optimal path (node sequence)
    - Total distance

8️⃣ Response Construction

- Routing Service formats output:
    - Path (node IDs)
    - Distance
    - Coordinates (if requested)
- API layer returns JSON response

9️⃣ Frontend Visualization

- Receives response
- Draw route on map using polyline
- Animates:
    - Route drawing
    - Moving marker
- Displays:
    - Distance
    - Visual path

---
## ⚙️ Special Handling

### 🔹 Grid Maps

- Coordinates are snapped to nearest valid node
- Prevents invalid routing requests

### 🔹 OSM Maps

- Uses real-world geographic coordinates
- Requires accurate node matching

### 🔹 Caching

- Graphs are loaded once and resused
- Improves performance for repeated requests

---

## 🚧 Failure Scenarios

- Invalid coordinates (too far from graph nodes)
- No valid path between nodes
- Incorrect map selection

---

## 💡 Key Insights

- Clear separation between:
    - API handling
    - Service orchestration
    - Algorithm execution
- Pipeline ensures:
    - Reusability
    - Extensibility
    - Debuggability

---

## ⏩ Future Improvements

- Real-time progress visualization of A*
- Dynamic cost functions (time, traffic)
- Enhanced error handling and user feedback