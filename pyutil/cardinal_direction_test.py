from pyutil.cardinal_direction import Direction, PrimaryFourDirections


def test_forward():
    assert Direction.East.forward(0, 0) == (0, 1)
    assert Direction.SouthEast.forward(0, 0) == (1, 1)
    assert Direction.NorthWest.forward(0, 0) == (-1, -1)


def test_turn():
    assert Direction.North.turn_left() == Direction.West
    assert Direction.North.turn_right() == Direction.East


def test_all_directions():
    assert PrimaryFourDirections == [
        Direction.North,
        Direction.East,
        Direction.South,
        Direction.West,
    ]
