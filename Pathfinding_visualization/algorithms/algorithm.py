from abc import ABC, abstractmethod


class Node:
    """
    Representation of maze field
    """

    def __init__(self, coord: tuple[int, int], parent: "Node"):
        self.coord = coord
        self.parent = parent


class AbstractAlgorithm(ABC):
    def __init__(self):
        self.found = False
        self.visited_fields = []
        self.found_path = []

    @abstractmethod
    def search(self):
        pass

    @abstractmethod
    def build_found_path(self):
        pass
