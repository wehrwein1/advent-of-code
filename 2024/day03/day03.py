import re
from typing import List
from collections import deque


class Solution:
    def computeDay(self, lines: List[str], part: int):

        def toggle_enabled(enabled, match, pos) -> bool:
            if enabled:
                i = memory.find("don't()", pos)
                if i != -1:
                    enabled = match.start() < i
            else:
                i = memory.find("do()", pos)
                if i != -1:
                    enabled = i < match.start()
            return enabled

        sum_ = 0
        enabled = True
        for memory in lines:
            matches = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", memory)
            if part == 1:
                for match in matches:
                    sum_ += int(match.group(1)) * int(match.group(2))
            elif part == 2:
                queue = deque(matches)
                pos = 0
                while queue:
                    match = queue.popleft()
                    enabled = toggle_enabled(enabled, match, pos)
                    if enabled:
                        sum_ += int(match.group(1)) * int(match.group(2))
                    pos = match.end()
        return sum_


# bootstrap
def main():
    print(f"part 1: {Solution().computeDay(readlines('2024/input/03_INPUT.txt'), 1)}")
    print(f"part 2: {Solution().computeDay(readlines('2024/input/03_INPUT.txt'), 2)}")


def readlines(path: str) -> List[str]:
    return [line.strip() for line in open(path)]


if __name__ == "__main__":
    main()
