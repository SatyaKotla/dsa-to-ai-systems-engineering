# 🚀 Route Optimization & Navigation System

## 📌 Overview

Route Optimization & Navigation service is a full-stack system for computing and visualizing optimal paths on graph-based maps using  algorithms such as A*.

It supports:
- Real-world navigation using OpenStreeMap (OSM)
- Synthetic grid-based graphs for testing and experimentation

This project is part of the DSA-to-AI-Systems-Engineering monrepo and integrates with the `butterbiscuit` project configuration.

---
## ✨ Features
- A* path finding for efficient shortest path computation
- 🗺️ Dual Map Support (OSM and Custome grid maps)
- 📍 Interactive Map UI (click to select routes)
- Animated Route Visualization with moving marker
- 📊 Distance Calculation
- 🧩 Modular Backend Architecture
- ⚙️ Configurable Map System
---
## 📚 Documentation

Detailed documentation is available in the [docs/](/dsa-to-ai-systems-engineering/docs/route_optimizer/) directory:

- [architecture.md](/dsa-to-ai-systems-engineering/docs/route_optimizer/architecture.md) -> system design and component interaction
- [routing_pipeline.md](/dsa-to-ai-systems-engineering/docs/route_optimizer/routing_pipeline.md) -> end-to-end routing flow
- [map_format.md](/dsa-to-ai-systems-engineering/docs/route_optimizer/map_format.md) -> graph and map data formats
- [api.md](/dsa-to-ai-systems-engineering/docs/route_optimizer/api.md)-> api specification

---
## 📂 Project Structure

    route_optimizer/
    │
    ├── api/                                    # FastAPI routes
    ├── config/                                 # Map configurations
    ├── data/                                   # Graph data & cache
    ├── engine/                                 # Core Logic (Algorithm and routing)
    ├── frontend/                               # UI layer
    │ ├── index.html
    │ ├── styles.css
    │ ├── script.js
    │ └── assets/
    │
    ├── loaders/                                # Graph loaders (OSM, JSON)
    │
    ├── scripts/                                # CLI / testing scripts
    │
    ├── services/                               # Map management
    ├── utils/                                  # Helper utilities
    └── README.md

---
## ⚙️ Setup Instructions

### 1. Backend

uvicorn system_design.route_optimizer.api.main:app --reload

### 2. Frontend

Run index.html using live server or:

python -m http.server 5500

Then open:

`http://localhost:5500` in your browser

---

## 🔌 API Example

### Endpoint

POST /route

### Request

    {
        "map": "grid_10",
        "start_lat": 0,
        "start_lon": 0,
        "end_lat": 5,
        "end_lon": 5,
        "cost": "distance",
        "include_coordinates": true
    }

### Response
    {
        "distance": 20.19,
        "path": ["n0_0", "n1_0", ...],
        "coordinates": [[lat, lon], ...]
    }

---
## 🚧 Status

This project is actively evolving as part of a broader system design and AI engineering pipeline.

---
## 🔮Roadmap
- A* exploration visualization
- Multi-route comparision
- Improved UI/UX
- Deployement and scaling

---
## 👨‍💻 Maintainer

* [@SatyaKotla](https://github.com/SatyaKotla)

---
## ⭐ Acknowledgements

- OpenStreetMap for map data
- Leaflet.js for frontend map rendering
