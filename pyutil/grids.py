from typing import List
from pyutil.cardinal_direction import Direction


def row_count(grid) -> int:
    return len(grid)


def col_count(grid) -> int:
    return len(grid[0])


def is_valid_coord(grid, rowIndex: int, colIndex: int) -> bool:
    rowOk = (0 <= rowIndex) and (rowIndex < row_count(grid))
    colOk = (0 <= colIndex) and (colIndex < col_count(grid))
    return rowOk and colOk


def walk(
    grid, start_row_index: int, start_col_index: int, direction: Direction
) -> List:
    r: int = start_row_index
    c: int = start_col_index
    walked_values = []
    while is_valid_coord(grid, r, c):
        walked_values.append(grid[r][c])
        r, c = direction.translate(r, c)
    return walked_values
