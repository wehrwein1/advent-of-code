from typing import List
from pyutil.fileio import file_lines


class Solution:
    def computeDay(self, lines: List[str], part: int):
        password = 0
        dial_size = 100
        dial_pos = 50
        for turn in lines:
            turn_dir, turn_distance = turn[0], int(turn[1:])
            is_left = turn_dir == "L"
            is_right = turn_dir == "R"
            for _ in range(turn_distance):
                if is_left:
                    dial_pos = (dial_pos - 1) % dial_size
                elif is_right:
                    dial_pos = (dial_pos + 1) % dial_size
                if part == 2 and dial_pos == 0:
                    password += 1
            if part == 1 and dial_pos == 0:
                password += 1
        return password


# bootstrap
def main():
    print(f"part 1: {Solution().computeDay(file_lines('2025/input/01_INPUT.txt'), 1)}")
    print(f"part 2: {Solution().computeDay(file_lines('2025/input/01_INPUT.txt'), 2)}")


if __name__ == "__main__":
    main()
