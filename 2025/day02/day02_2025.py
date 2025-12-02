import re
from typing import List
from pyutil.fileio import file_lines


class Solution:
    def computeDay(self, lines: List[str], part: int):
        DEBUG = False
        invalid_ids = []
        product_ranges = [line.strip() for line in lines[0].split(",")]
        if DEBUG:
            print(f"part={part}")
        for product_range in product_ranges:
            low, high = list(map(int, product_range.split("-")))
            if DEBUG:
                print(f"range={[low, high]}")
            for product_id in range(low, high + 1):
                match: re.Match = re.fullmatch(r"(\d{1,})\1+", str(product_id))
                if match:
                    matched_text = match.group(0)
                    match_len = len(matched_text)
                    is_invalid = (
                        match_len == len(str(product_id))
                        and matched_text[0 : match_len // 2]
                        == matched_text[match_len // 2 :]
                    )
                    if is_invalid:
                        if DEBUG:
                            print(
                                f" invalid product_id: '{product_id}' with match='{matched_text}' len_={match_len}"
                            )
                        invalid_ids.append(product_id)

        return sum(invalid_ids) if part == 1 else -1


# bootstrap
def main():
    print(f"part 1: {Solution().computeDay(file_lines('2025/input/02_INPUT.txt'), 1)}")
    print(f"part 2: {Solution().computeDay(file_lines('2025/input/02_INPUT.txt'), 2)}")


if __name__ == "__main__":
    main()
