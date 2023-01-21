import turtle

from trunic.trunic_character import TrunicCharacter
from point import Point
import constant.constant as constant


def draw(pen: turtle.Turtle, character: TrunicCharacter, center: Point = Point(0, 0), scale: float = 1):
    for i, edge in enumerate(character.get_edges()):
        if not edge:
            continue
        pen.penup()
        points: tuple[Point, Point] = constant.SEGMENT_INDEX_TO_POINTS[i]
        start_point: Point = center + points[0] * scale
        end_point: Point = center + points[1] * scale
        pen.goto(start_point.x, start_point.y)
        pen.pendown()
        pen.goto(end_point.x, end_point.y)
        pen.penup()