from abc import ABC, abstractmethod


class BaseMapLoader(ABC):
    """
    Base interface for all map loaders.
    """

    @abstractmethod
    def load(self, source: str):
        """
        Load a map and return a Graph.
        """
        pass
