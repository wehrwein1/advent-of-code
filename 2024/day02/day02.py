from typing import List


class Solution:

    def check_safe(self, deltas: List[int]) -> bool:
        in_value_range = lambda n: 1 <= abs(n) and abs(n) <= 3
        is_positive = lambda n: n > 0
        is_negative = lambda n: n < 0
        # fmt:off
        return all(map(in_value_range, deltas)) and \
                (all(map(is_positive, deltas)) or \
                 all(map(is_negative, deltas)))
        # fmt:on

    def make_deltas(self, values: List[int]) -> List[int]:
        deltas = []
        for i in range(1, len(values)):
            pair = values[i - 1 : i + 1]
            delta = pair[0] - pair[1]
            deltas.append(delta)
        return deltas

    def computeDay(self, lines: List[str], part: int):
        safe_count = 0
        for line in lines:
            values = list(map(int, line.split()))
            if part == 1:
                deltas = self.make_deltas(values)
                is_safe = self.check_safe(deltas)
            elif part == 2:
                n = len(values)
                for i in range(n):
                    values_ = values.copy()
                    del values_[i]
                    deltas = self.make_deltas(values_)
                    is_safe = self.check_safe(deltas)
                    if is_safe:
                        break
            print(f"line: [{line}], safe: {is_safe}")
            if is_safe:
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
