import itertools
from typing import List
from pyutil.fileio import file_lines


class Solution:
    def computeDay(self, lines: List[str], part: int):
        joltages = []
        for rating in lines:
            numbers = list(rating)
            if part == 1:
                result = -1
                for combo in itertools.combinations(numbers, 2):
                    result = max(result, int("".join(combo)))
            elif part == 2:
                batteries = list(map(int, rating))
                # adapted from https://www.reddit.com/r/adventofcode/comments/1pd0pmt/comment/ns2juje
                # intuition: repeatedly scan for largest digit, each iteration time O(n)
                start = 0
                result_digits = []
                length = len(batteries)
                max_batteries = 12
                for digit_pos in range(max_batteries):
                    end = length - (max_batteries - digit_pos) + 1
                    max_digit = max(batteries[start:end])
                    result_digits.append(
                        max_digit
                    )  # better: build final number inline: `result = result * 10 + max_digit`
                    start = batteries.index(max_digit, start, end) + 1
                result = int("".join(map(str, result_digits)))
            # print(f"{rating} -> {result}")
            joltages.append(result)
        return sum(joltages)


# bootstrap
def main():
    print(f"part 1: {Solution().computeDay(file_lines('2025/input/03_INPUT.txt'), 1)}")
    print(f"part 2: {Solution().computeDay(file_lines('2025/input/03_INPUT.txt'), 2)}")


if __name__ == "__main__":
    main()
