from constant.edges import Edge
from point import Point
from typing import Tuple, Dict

# Turtle is upside-down graphics-wise
TOP = Point(0, -1.5)
MID_TOP = Point(0, -0.5)
MID_BOTTOM = Point(0, 0.5)
BOTTOM = Point(0, 1.5)
LEFT_TOP = Point(-1, -1)
LEFT_BOTTOM = Point(-1, 1)
RIGHT_TOP = Point(1, -1)
RIGHT_BOTTOM = Point(1, 1)

EDGE_TO_POINTS: Dict[Edge, Tuple[Point, Point]] = {
    Edge.IN_UP: (MID_TOP, TOP),
    Edge.IN_UP_RIGHT: (MID_TOP, RIGHT_TOP),
    Edge.IN_UP_LEFT: (MID_TOP, LEFT_TOP),
    Edge.IN_MID: (MID_TOP, MID_BOTTOM),
    Edge.IN_DOWN: (MID_BOTTOM, BOTTOM),
    Edge.IN_DOWN_RIGHT: (MID_BOTTOM, RIGHT_BOTTOM),
    Edge.IN_DOWN_LEFT: (MID_BOTTOM, LEFT_BOTTOM),
    Edge.OUT_LEFT: (LEFT_TOP, LEFT_BOTTOM),
    Edge.OUT_UP_LEFT: (LEFT_TOP, TOP),
    Edge.OUT_UP_RIGHT: (RIGHT_TOP, TOP),
    Edge.OUT_DOWN_LEFT: (LEFT_BOTTOM, BOTTOM),
    Edge.OUT_DOWN_RIGHT: (RIGHT_BOTTOM, BOTTOM),
}