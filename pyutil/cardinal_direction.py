from enum import Enum, auto
from typing import Tuple


# see https://docs.python.org/3/howto/enum.html
class Direction(Enum):
    North = auto()
    NorthEast = auto()
    East = auto()
    SouthEast = auto()
    South = auto()
    SouthWest = auto()
    West = auto()
    NorthWest = auto()

    def translate(self, row: int, col: int) -> Tuple[int, int]:
        # 4 main directions
        if self == Direction.North:
            return row - 1, col
        elif self == Direction.East:
            return row, col + 1
        elif self == Direction.South:
            return row + 1, col
        elif self == Direction.West:
            return row, col - 1
        # diagonals
        elif self == Direction.NorthEast:
            return row - 1, col + 1
        elif self == Direction.SouthEast:
            return row + 1, col + 1
        elif self == Direction.SouthWest:
            return row + 1, col - 1
        elif self == Direction.NorthWest:
            return row - 1, col - 1
        else:
            raise SystemError(f"unknown direction case: {self}")

    def turn_left(self):
        return PrimaryFourDirections[(PrimaryFourDirections.index(self) - 1) % 4]

    def turn_right(self):
        return PrimaryFourDirections[(PrimaryFourDirections.index(self) + 1) % 4]


PrimaryFourDirections = [
    Direction.North,
    Direction.East,
    Direction.South,
    Direction.West,
]
AllDirections = [d for d in Direction]
