class MapValidator:

    @staticmethod
    def validate(data):

        if "nodes" not in data:
            raise ValueError("Map file missing 'nodes'")

        if "edges" not in data:
            raise ValueError("Map file missing 'edges'")

        nodes = data["nodes"]

        for edge in data["edges"]:

            if isinstance(edge, list):
                u, v, _ = edge

            elif isinstance(edge, dict):
                u = edge["from"]
                v = edge["to"]

            else:
                raise ValueError("Invalid edge format")

            if u not in nodes:
                raise ValueError(f"Edge reference unknown node: {u}")

            if v not in nodes:
                raise ValueError(f"Edge reference unknown node: {v}")
