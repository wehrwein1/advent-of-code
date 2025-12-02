import re
from typing import List
from pyutil.fileio import file_lines


class Solution:
    def computeDay(self, lines: List[str], part: int):
        DEBUG = False
        part1_regex = r"(\d+)\1"  # a digit pattern exactly twice
        part2_regex = r"(\d+)\1+"  # a digit pattern at least twice
        invalid_ids = []
        product_ranges = [line.strip() for line in lines[0].split(",")]
        if DEBUG:
            print(f"part={part}")
        regex = part1_regex if part == 1 else part2_regex
        for product_range in product_ranges:
            low, high = list(map(int, product_range.split("-")))
            if DEBUG:
                print(f"range={[low, high]}")
            for product_id in range(low, high + 1):
                match: re.Match = re.fullmatch(regex, str(product_id))
                is_invalid = match is not None
                if is_invalid:
                    if DEBUG:
                        print(f"'{product_id}'")
                    invalid_ids.append(product_id)
        return sum(invalid_ids)


# bootstrap
def main():
    print(f"part 1: {Solution().computeDay(file_lines('2025/input/02_INPUT.txt'), 1)}")
    print(f"part 2: {Solution().computeDay(file_lines('2025/input/02_INPUT.txt'), 2)}")


if __name__ == "__main__":
    main()
