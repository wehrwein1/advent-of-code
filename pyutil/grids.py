from collections import deque
from typing import Deque, List, Callable, Any, Set, Tuple
from pyutil.cardinal_direction import Direction


def row_count(grid) -> int:
    return len(grid)


def col_count(grid) -> int:
    return len(grid[0])


def dim(grid: List[List]) -> Tuple[int, int]:
    return (row_count(grid), col_count(grid))


def is_valid_coord(grid, rowIndex: int, colIndex: int) -> bool:
    rowOk = (0 <= rowIndex) and (rowIndex < row_count(grid))
    colOk = (0 <= colIndex) and (colIndex < col_count(grid))
    return rowOk and colOk


def __extract_value(grid, r, c):
    return grid[r][c]


def walk(
    grid: List[List],
    start_row_index: int,
    start_col_index: int,
    direction: Direction,
    can_walk: Callable[[List[List], int, int], bool] = is_valid_coord,
    collect_value_function: Callable[[List[List], int, int], Any] = __extract_value,
) -> Tuple[List[List], Tuple[int, int]]:
    """
    Traverse grid in a specified direction.
    Return colected values and end position (tuple)
    """
    r: int = start_row_index
    c: int = start_col_index
    walked_values = []
    while can_walk(grid, r, c):
        value = collect_value_function(grid, r, c)
        walked_values.append(value)
        r, c = direction.walk_forward(r, c)
    return (walked_values, (r, c))


def find_neighbors(
    grid: List[List],
    r: int,
    c: int,
    searchDirections: List[Direction] = list(Direction),
) -> List[Tuple[int, int]]:
    neighbors: List[Tuple[int, int]] = []
    for direction in searchDirections:
        row, col = direction.walk_forward(r, c)
        if is_valid_coord(grid, row, col):
            neighbors.append((row, col))
    return neighbors


def search(
    grid: List[List],
    query: Callable[
        [List[List], Tuple[int, int], List[Tuple[int, int]]], bool
    ],  # grid, originPoint, neighborPoints
    searchDirections: List[Direction] = list(Direction),
    # collect_value_function: Callable[[List[List], int, int], Any] = __extract_value,
) -> List[Tuple[int, int]]:
    """
    Search a grid, return coordinates that match a predicate
    """
    matches = []
    visited: Set[Tuple[int, int]] = set()
    # reachablePoints: Set[Tuple[int, int]] = set()
    queue: Deque[Tuple[int, int]] = deque()
    queue.append((0, 0))  # start at top-left corner
    while queue:
        r, c = queue.popleft()
        originPoint = (r, c)
        if originPoint in visited:
            continue
        neighbors: List[Tuple[int, int]] = find_neighbors(grid, r, c, searchDirections)
        for neighbor in neighbors:
            if not neighbor in visited:
                queue.append(neighbor)
        if query(grid, originPoint, neighbors):
            matches.append(originPoint)
        visited.add(originPoint)
    return matches
