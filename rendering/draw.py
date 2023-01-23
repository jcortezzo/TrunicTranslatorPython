import turtle

from trunic.trunic_character import TrunicCharacter
from constant.edges import Edge
from rendering.points import EDGE_TO_POINTS

from point import Point

def draw(pen: turtle.Turtle, character: TrunicCharacter, center: Point = Point(0, 0), scale: float = 1):
    def drawEdge(e: Edge) -> None:
        pen.penup()
        (start, end) = EDGE_TO_POINTS[e]
        start_point: Point = center + start * scale
        end_point: Point = center + end * scale
        pen.goto(start_point.x, start_point.y)
        pen.pendown()
        pen.goto(end_point.x, end_point.y)
        pen.penup()

    for e in character.get_edges():
        drawEdge(e)