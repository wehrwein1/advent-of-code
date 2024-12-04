from pyutil.cardinal_direction import Direction, PrimaryFourDirections


def test_translate():
    assert Direction.East.translate(0, 0) == (0, 1)
    assert Direction.SouthEast.translate(0, 0) == (1, 1)
    assert Direction.NorthWest.translate(0, 0) == (-1, -1)


def test_all_directions():
    assert PrimaryFourDirections == [
        Direction.North,
        Direction.East,
        Direction.South,
        Direction.West,
    ]
