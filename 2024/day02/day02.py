from typing import List


class Solution:
    def computeDay(self, lines: List[str], part: int):
        safe_count = 0
        for line in lines:
            deltas = []
            values = list(map(int, line.split()))
            for i in range(1, len(values)):
                pair = values[i - 1 : i + 1]
                delta = pair[0] - pair[1]
                deltas.append(delta)

            in_value_range = lambda n: 1 <= abs(n) and abs(n) <= 3
            is_positive = lambda n: n > 0
            is_negative = lambda n: n < 0
            if part == 1:
                # fmt:off
                safe = all(map(in_value_range, deltas)) and \
                       (all(map(is_positive, deltas)) or \
                        all(map(is_negative, deltas)))
                # fmt:on
            else:
                # fmt:off
                n = len(deltas)
                allowed = [n-1, n]
                safe = len(list(map(in_value_range, deltas))) in allowed and \
                       (len(list(map(is_positive, deltas))) in allowed) or \
                        len(list(map(is_negative, deltas))) in allowed
                # fmt:on
            print(f"line: [{line}], safe: {safe}")
            if safe:
                safe_count += 1
        return safe_count


# bootstrap
def main():
    print(f"part 1: {Solution().computeDay(readlines('2024/input/02_INPUT.txt'), 1)}")
    print(f"part 2: {Solution().computeDay(readlines('2024/input/02_INPUT.txt'), 2)}")


def readlines(path: str) -> List[str]:
    return [line.strip() for line in open(path)]


if __name__ == "__main__":
    main()
