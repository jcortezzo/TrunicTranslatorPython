class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point') -> 'Point':
        negative_other = Point(-other.x, -other.y)
        return self + other

    def __mul__(self, constant: float) -> 'Point':
        return Point(self.x * constant, self.y * constant)