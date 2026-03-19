from system_design.route_optimizer.loaders.json_loader import JSONMapLoader


class MapLoader:

    @staticmethod
    def from_json(file_path, cost_model=None):
        loader = JSONMapLoader(cost_model=cost_model)
        return loader.load(file_path)
