import itertools
from typing import List
from pyutil.fileio import file_lines


class Solution:
    def computeDay(self, lines: List[str], part: int):
        joltages = []
        for rating in lines:
            numbers = list(rating)
            if part == 1:
                max_ = -1
                for combo in itertools.combinations(numbers, 2):
                    max_ = max(max_, int("".join(combo)))
                print(f"{rating} -> {max_}")
                joltages.append(max_)
            elif part == 2:
                pass
        return sum(joltages)


# bootstrap
def main():
    print(f"part 1: {Solution().computeDay(file_lines('2025/input/03_INPUT.txt'), 1)}")
    print(f"part 2: {Solution().computeDay(file_lines('2025/input/03_INPUT.txt'), 2)}")


if __name__ == "__main__":
    main()
