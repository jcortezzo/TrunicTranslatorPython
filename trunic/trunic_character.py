import constant.constant as constant
from constant.edges import Edge
from typing import FrozenSet

Edges = FrozenSet[Edge]

class TrunicCharacter:

    def __init__(self, character: str) -> None:
        self.__edges: list[bool] = constant.IPA_TO_TRUNIC_EDGES[character]

    def get_edges(self) -> list[bool]:
        return self.__edges