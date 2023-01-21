from point import Point

IPA_TO_TRUNIC_EDGES: dict[str, list[bool]] = {
    "æ": [True] * 2 + [False] * 3 + [True],#[True, True, False, False, False, True],
    "ɑr": [True] * 2 + [False] * 8 + [True] * 2
}

# Turtle is upside-down graphics-wise
POINT_COORDS_ON_SCREEN: list[Point] = [
    Point(-1, 1),
    Point( 0, 1.5),
    Point( 1, 1),

    # Point(-1, -1),
    # Point( 0, -1.5),
    # Point( 1, -1),

    Point( 0, -0.5),
    Point( 0,  0.5),

    # Point( 1,  1),
    # Point( 0,  1.5),
    # Point(-1,  1),

    Point(-1,  -1),
    Point( 0,  -1.5),
    Point( 1,  -1),
]

SEGMENT_INDEX_TO_POINTS: list[(Point, Point)] = [
    (POINT_COORDS_ON_SCREEN[0], POINT_COORDS_ON_SCREEN[1]),
    (POINT_COORDS_ON_SCREEN[1], POINT_COORDS_ON_SCREEN[2]),
    (POINT_COORDS_ON_SCREEN[0], POINT_COORDS_ON_SCREEN[3]),
    (POINT_COORDS_ON_SCREEN[1], POINT_COORDS_ON_SCREEN[3]),
    (POINT_COORDS_ON_SCREEN[2], POINT_COORDS_ON_SCREEN[3]),
    (POINT_COORDS_ON_SCREEN[0], POINT_COORDS_ON_SCREEN[5]),
    (POINT_COORDS_ON_SCREEN[3], POINT_COORDS_ON_SCREEN[4]),
    (POINT_COORDS_ON_SCREEN[4], POINT_COORDS_ON_SCREEN[5]),
    (POINT_COORDS_ON_SCREEN[4], POINT_COORDS_ON_SCREEN[6]),
    (POINT_COORDS_ON_SCREEN[4], POINT_COORDS_ON_SCREEN[7]),
    (POINT_COORDS_ON_SCREEN[5], POINT_COORDS_ON_SCREEN[6]),
    (POINT_COORDS_ON_SCREEN[6], POINT_COORDS_ON_SCREEN[7]),
]