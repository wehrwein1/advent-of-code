from pyutil.cardinal_direction import Direction, PrimaryFourDirections


def test_walk_forward():
    assert Direction.East.walk_forward(0, 0) == (0, 1)
    assert Direction.SouthEast.walk_forward(0, 0) == (1, 1)
    assert Direction.NorthWest.walk_forward(0, 0) == (-1, -1)


def test_walk_backward():
    assert Direction.East.walk_backward(0, 0) == (0, -1)
    assert Direction.SouthEast.walk_backward(0, 0) == (-1, -1)
    assert Direction.NorthWest.walk_backward(0, 0) == (1, 1)


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
