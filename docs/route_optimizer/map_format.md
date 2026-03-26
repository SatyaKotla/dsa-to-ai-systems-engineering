# 🗺️ Map Format Specification

## 📌 Overview

This document defines how maps are represented and consumed within the Route Optimization and Navigation System.

The system supports multiple map types through a unified graph abstraction:

- Grid-based maps (custom JSON format)
- OpenStreetMap (OSM) data

All map types are converted into a graph structure that can be processed by a routing engine.

---

## 🧠 Core Graph Model

Regardless of the source, every map is represented as:

Graph = (Nodes, Edges)

### 🔹 Nodes
- Represent locations (points in space)
- Identified by unique IDs
- Store coordinate information

### 🔹 Edges
- Represent connection between nodes
- Store traversal cost (e.g.,  distance)
- Can be directed or undirected

---

## ▦ Grid Map Format (JSON)

Grid maps are synthetic datasets used for testing and experimentation.

### 🔹 Structure

    {
        "nodes": {
            "n0_0": [0, 0],
            "n0_1": [0, 1],
            "n1_0": [1, 0]
        },

        "edges": [
            ["n0_0", "n1_0", 1],
            ["n0_0", "n0_1", 1]
        ]
    }

### 🔹 Node Format

    node_id → [x, y]

- node_id: Unique identifier (e.g., n0_0)
- [x, y]: Grid coordinates

### 🔹 Edge Format

    Edge → [source_node, target_node, weight]

- source_node: Starting node ID
- target_node: Destination node ID
- weight: Cost of traversal

### 🔹 Grid Properties

- Nodes are arranged in N x N grid
- Edges typically connect:
    - Right neighbor
    - Bottom neighbor

### 🔹 Directed vs Undirected

- Current implementation uses undirected edges
- Ensuring traversal in top, down, left and right directions

### 🔹 Coordinate System

- Grid coordinates are treated as:
    - (x, y) positions
- Mapped to:
    - (lat, lon) in frontend visualization

---

## 🌍 OpenStreetMap (OSM) Format

OSM data represents real-world geographic maps.

### 🔹 Conceptual Model

- Nodes → geographic coordinates (latitude, longitude)
- Edges → road segments between nodes

### 🔹 Characteristics

- Irregualar graph (not grid-based)
- Real-world distances and topology
- Large-scale datasets

### 🔹 Processing

OSM data is:

1. Parsed by a loader
2. Converted into internal graph format
3. Stored as:
    - Node dictionary
    - Edge list / adjacency structure

---

## 🔄 Unified Graph Representation

Both Grid and OSM maps are converted into:

    nodes: Dict[node_id → (lat, lon)]
    edges: adjacency structure with weights

---

## 📍 Coordinate Handling

### 🔹 Grid Maps

- Coordinates must match node positions
- Frontend applies snapping to nearest valid node

### 🔹 OSM Maps

- Coordinates are continuous
- Nearest node lookup is required

---

## ⚙️ Loader Responsibilities

Loaders are responsible for:

- Parsing raw data
- Constructing graph structures
- Ensuring consistency in node and edge formats

---

## 🚧 Constraints and Assumptions

- Node IDs must be unique
- Edge weights must be non-negative
- Graph must be connected for well routing
- Coordinates must map to valid nodes

---

## 🧠 Design Decisions

### ✔️ Unified Graph Interface

All map types conform to the same internal structure.

### ✔️ Pluggable loaders

New map formats can be added without modifying the routing engine.

### ✔️ Explicit Edge Definition

Edges are defined explicitly to maintain flexibility.

---

## ⏩ Future Enhancements

- Support for:
    - Travel Time
    - Traffic Conditions
    - Dynamic graph updates
- Integration with:
    - External map APIs

---

## 💡 Key Insights

- Maps are abstracted as graphs
- Grid and OSM share a unified interface
- Loaders isolate data format comlexity
- Routing engine remains independent of map source