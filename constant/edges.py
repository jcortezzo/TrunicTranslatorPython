from enum import Enum, auto
from typing import FrozenSet

class Edge(Enum):
    IN_UP = auto()
    IN_UP_RIGHT = auto()
    IN_UP_LEFT = auto()
    IN_MID = auto()
    IN_DOWN = auto()
    IN_DOWN_RIGHT = auto()
    IN_DOWN_LEFT = auto()
    OUT_LEFT = auto()
    OUT_UP_LEFT = auto()
    OUT_UP_RIGHT = auto()
    OUT_DOWN_LEFT = auto()
    OUT_DOWN_RIGHT = auto()

Edges = FrozenSet[Edge]

CONSONANTS: Edges = frozenset(Edge.IN_UP, Edge.IN_UP_LEFT, Edge.IN_UP_RIGHT, Edge.IN_MID, Edge.IN_DOWN, Edge.IN_DOWN_LEFT, Edge.IN_DOWN_RIGHT)
VOWELS: Edges = frozenset(Edge.OUT_LEFT, Edge.OUT_DOWN_LEFT, Edge.OUT_UP_LEFT, Edge.OUT_UP_RIGHT, Edge.OUT_DOWN_RIGHT)