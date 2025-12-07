from typing import List
from pyutil.fileio import file_lines


class Solution:
    def computeDay(self, lines: List[str], part: int):
        bathroom_code = 0
        button = 5
        for line in lines:
            print(f"start {button}")
            for dir in line:
                if dir == "U":
                    if button > 3:  # higher row
                        button -= 3
                elif dir == "D":
                    if button < 7:  # lower row
                        button += 3
                elif dir == "L":
                    if button > 1:
                        button -= 1
                elif dir == "R":
                    if button < 9:
                        button += 1
                print(f" {dir} -> {button}")
            bathroom_code = (bathroom_code * 10) + button
            print(f"'{line}' -> {button}, code={bathroom_code}")
        return bathroom_code


# bootstrap
def main():
    print(f"part 1: {Solution().computeDay(file_lines('2016/input/02_INPUT.txt'), 1)}")
    # print(f"part 2: {Solution().computeDay(file_lines('2016/input/02_INPUT.txt'), 2)}")


if __name__ == "__main__":
    main()
