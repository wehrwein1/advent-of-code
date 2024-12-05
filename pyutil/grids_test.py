from pyutil.grids import walk, row_count, col_count, is_valid_coord
from pyutil.cardinal_direction import Direction


# fmt:off
grid = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9],
        [10,11,12]]
# fmt:on


def test_counts():
    assert row_count(grid) == 4
    assert col_count(grid) == 3


def test_is_valid_coord():
    assert is_valid_coord(grid, 0, 0) == True
    assert is_valid_coord(grid, -1, 0) == False
    assert is_valid_coord(grid, 3, 2) == True  # lowest right
    assert is_valid_coord(grid, 0, 3) == False  # out of bounds (col)
    assert is_valid_coord(grid, 4, 0) == False  # out of bounds (row)


def test_walk():
    assert walk(grid, 0, 0, Direction.North) == [1]
    assert walk(grid, 0, 0, Direction.West) == [1]
    assert walk(grid, 0, 0, Direction.South) == [1, 4, 7, 10]
    assert walk(grid, 0, 0, Direction.SouthEast) == [1, 5, 9]
