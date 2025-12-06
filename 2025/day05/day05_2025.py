from itertools import pairwise
from typing import List
from pyutil.fileio import file_lines
from pyutil.strings import partition


class Solution:

    def overlaps(self, a, b) -> bool:
        end_a, end_b = a[1], b[1]
        start_a, start_b = a[0], b[0]
        # https://www.google.com/search?q=formula+for+boolean+overlapping+range
        #     [----a----]
        #           [----b----]
        has_overlap = start_a <= end_b and start_b <= end_a
        return has_overlap

    def adjacent(self, a, b) -> bool:
        # implied: a start <= b start
        return a[1] + 1 == b[0]

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
            # print(f"ingredient_ids: {ingredient_ids}")
            for ingredient_id in ingredient_ids:
                for range_ in ranges:
                    is_fresh = ingredient_id in range(range_[0], range_[1] + 1)
                    if is_fresh:
                        # print(f"{ingredient_id} is fresh in {range_}")
                        count_fresh += 1
                        break
        elif part == 2:
            any_merged = True
            while any_merged:
                any_merged = False
                i = 0
                while i < len(ranges) - 1:
                    a = ranges[i]
                    b = ranges[i + 1]
                    if self.overlaps(a, b) or self.adjacent(a, b):
                        # merge
                        low = a[0]  # because sorted
                        high = max(a[1], b[1])
                        new_range = (low, high)
                        # print(f"Merging {a} and {b} into {new_range}")
                        ranges[i] = new_range
                        del ranges[i + 1]
                        any_merged = True
                    else:
                        i += 1
            for range_ in ranges:
                len_ = self.range_len(range_)
                # print(f"{range_=} len={len_}")
                count_fresh += len_

        return count_fresh


# bootstrap
def main():
    print(f"part 1: {Solution().computeDay(file_lines('2025/input/05_INPUT.txt'), 1)}")
    print(f"part 2: {Solution().computeDay(file_lines('2025/input/05_INPUT.txt'), 2)}")


if __name__ == "__main__":
    main()
