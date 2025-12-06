from math import log10
from typing import List
from pyutil.fileio import file_lines
from pyutil.ints import product


class Solution:
    def computeDay(self, lines: List[str], part: int):
        problems = [list(map(int, line.split())) for line in lines[:-1]]
        operators = lines[-1].split()
        print(f"{problems=} {operators=}")
        total = 0
        n = len(problems[0])
        for i in range(n):
            op = operators[i]
            values = [p[i] for p in problems]
            if part == 2:
                pass
            if op == "+":
                result = sum(values)
            elif op == "*":
                result = product(values)
            print(f"{i} '{op}' {values} -> result={result}")
            total += result
        print(problems, operators)
        return total


# bootstrap
def main():
    print(f"part 1: {Solution().computeDay(file_lines('2025/input/06_INPUT.txt'), 1)}")
    print(f"part 2: {Solution().computeDay(file_lines('2025/input/06_INPUT.txt'), 2)}")


if __name__ == "__main__":
    main()
