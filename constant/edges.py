from enum import Enum, auto

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

class ConsonantEdge(Enum):
    UP = Edge.IN_UP
    UP_RIGHT = Edge.IN_UP_RIGHT
    UP_LEFT = Edge.IN_UP_LEFT
    MID = Edge.IN_MID
    DOWN = Edge.IN_DOWN
    DOWN_RIGHT = Edge.IN_DOWN_RIGHT
    DOWN_LEFT = Edge.IN_DOWN_LEFT

class VowelEdge(Enum):
    LEFT = Edge.OUT_LEFT
    UP_LEFT = Edge.OUT_UP_LEFT
    UP_RIGHT =  Edge.OUT_UP_RIGHT
    DOWN_LEFT = Edge.OUT_DOWN_LEFT
    DOWN_RIGHT = Edge.OUT_DOWN_RIGHT