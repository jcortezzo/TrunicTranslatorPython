import turtle

from trunic.trunic_character import TrunicCharacter
from trunic.trunic_word import TrunicWord
from point import Point
import constant.constant as constant

def draw_word(pen: turtle.Turtle, word: TrunicWord, center: Point = Point(0, 0), scale: float = 1):
    for character in word.get_characters():
        draw_character(pen, character, center=center, scale=scale)
        center = center + Point(2, 0) * scale

def draw_character(pen: turtle.Turtle, character: TrunicCharacter, center: Point = Point(0, 0), scale: float = 1):
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