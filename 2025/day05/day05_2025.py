from itertools import pairwise
from typing import List
from pyutil.fileio import file_lines
from pyutil.strings import partition


class Solution:

    def overlap(self, a, b) -> int:
        # https://www.google.com/search?q=range+overlap+formula
        end_a, end_b = a[1], b[1]
        start_a, start_b = a[0], b[0]
        return max(0, min(end_a, end_b) + 1 - max(start_a, start_b))  # +1 = inclusive

    def range_len(self, r) -> int:
        return r[1] - r[0] + 1  # +1 = inclusive

    def computeDay(self, lines: List[str], part: int):

        def parse_int_range(s: str):
            a, b = s.split("-")
            return (int(a), int(b))

        ranges_, ingredient_ids_ = partition(lines)
        ranges = sorted(map(parse_int_range, ranges_))
        count_fresh = 0
        # print(f"ingredient ranges: {ranges}")
        if part == 1:
            ingredient_ids = [int(x) for x in ingredient_ids_]
            print(f"ingredient_ids: {ingredient_ids}")
            for ingredient_id in ingredient_ids:
                for range_ in ranges:
                    is_fresh = ingredient_id in range(range_[0], range_[1] + 1)
                    if is_fresh:
                        print(f"{ingredient_id} is fresh in {range_}")
                        count_fresh += 1
                        break
        elif part == 2:
            for a, b in pairwise(ranges):
                overlap_ = self.overlap(a, b)
                len_ = self.range_len(b) - overlap_
                is_first = a == ranges[0]
                if is_first:
                    len_ += self.range_len(a)
                print(f"ranges {a} and {b} overlap: {overlap_} count +{len_}")
                count_fresh += len_

        return count_fresh


# bootstrap
def main():
    print(f"part 1: {Solution().computeDay(file_lines('2025/input/05_INPUT.txt'), 1)}")
    print(f"part 2: {Solution().computeDay(file_lines('2025/input/05_INPUT.txt'), 2)}")


if __name__ == "__main__":
    main()
