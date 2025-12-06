from math import log10
from typing import List, Tuple
from pyutil.ints import product


class Solution:
    def parse(self, lines: List[str]) -> Tuple[List[List[str]], List[str]]:
        problems_lines_ = lines[:-1]
        operators_line_ = lines[-1]
        problems: List[List[str]] = [[] for _ in problems_lines_]
        operators: List[str] = []
        n = len(operators_line_)

        def collect_problems(problems: List, start: int, length: int) -> None:
            for i in range(len(problems_lines_)):
                value = problems_lines_[i][start : start + length]
                problems[i].append(value)

        start, i = 0, 0
        while i < n:
            if operators_line_[i] in "+*":
                op = operators_line_[i]
                operators.append(op)
                i += 1
                while i < n and operators_line_[i] == " ":  # consume whitespace
                    i += 1
                token_length = i - start
                if i != n:
                    token_length -= 1  # trim inner delimiter whitespaces
                collect_problems(problems, start=start, length=token_length)
                start = i
                continue
            i += 1
        return problems, operators

    def computeDay(self, lines: List[str], part: int) -> int:
        problems, operators = self.parse(lines)
        print(f"{problems=} {operators=}")
        total = 0
        n = len(problems[0])
        for col in range(n):
            op = operators[col]
            if part == 1:
                col_values = [int(p[col].strip()) for p in problems]
            if part == 2:
                digits = len(problems[0][col])
                padded_values = [int(row[col].replace(" ", "0")) for row in problems]
                col_values = []
                # each digit place
                for d in range(digits, 0, -1):
                    digit_mask = 10 ** (d - 1)
                    # each vertical value
                    col_value = 0
                    i = 0
                    while i < len(padded_values):
                        value = padded_values[i]
                        div, mod = divmod(value, digit_mask)
                        if div:
                            col_value = (col_value * 10) + div
                            padded_values[i] = mod
                        i += 1
                    col_values.append(col_value)
            if op == "+":
                result = sum(col_values)
            elif op == "*":
                result = product(col_values)
            print(f"{col} '{op}' {col_values} -> result={result}")
            total += result
        return total


# custom file_lines() parse function, re: trailing whitespace is important
def file_lines(filename: str) -> List[str]:
    return [line.rstrip("\n") for line in open(filename)]


# bootstrap
def main():
    print(f"part 1: {Solution().computeDay(file_lines('2025/input/06_INPUT.txt'), 1)}")
    print(f"part 2: {Solution().computeDay(file_lines('2025/input/06_INPUT.txt'), 2)}")


if __name__ == "__main__":
    main()
