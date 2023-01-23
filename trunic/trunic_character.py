from constant.edges import Edge, Edges
from constant.sounds import IPA_TO_TRUNIC_EDGES
from typing import FrozenSet

Edges = FrozenSet[Edge]

class TrunicCharacter:
    def __init__(self, character: str) -> None:
        self.__edges: Edges = IPA_TO_TRUNIC_EDGES[character]

    def get_edges(self) -> Edges:
        return self.__edges