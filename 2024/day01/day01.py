from typing import Counter, List


class Solution:
    def computeDay(self, lines: List[str], part: int):
        l1 = []
        l2 = []
        for line in lines:
            first, second = map(int, line.split())
            l1.append(first)
            l2.append(second)
        l1.sort()
        l2.sort()
        assert len(l1) == len(l2)

        sum = 0
        if part == 1:
            for pair in zip(l1, l2):
                sum += abs(pair[0] - pair[1])
        else:
            counts = Counter(l2)
            for left in l1:
                sum += left * counts[left]

        return sum


# bootstrap
def main():
    print(
        f"part 1: {Solution().computeDay(list(map(str.rstrip, open('input/01_INPUT.txt'))), 1)}"
    )
    print(
        f"part 2: {Solution().computeDay(list(map(str.rstrip, open('input/01_INPUT.txt'))), 2)}"
    )


if __name__ == "__main__":
    main()
