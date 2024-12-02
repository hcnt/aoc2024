from itertools import pairwise


def main():
    with open("input.txt", "r") as f:
        values = f.readlines()
        result_part1 = 0
        result_part2 = 0
        for line in values:
            numbers = list(map(int, line.split()))
            if not numbers:
                continue
            difs = list(map(lambda x: x[1] - x[0], pairwise(numbers)))
            if all(0 < dif < 4 for dif in difs) or all(-4 < dif < 0 for dif in difs):
                result_part1 += 1

            for i in range(len(numbers)):
                val = numbers.pop(i)
                difs = list(map(lambda x: x[1] - x[0], pairwise(numbers)))
                if all(0 < dif < 4 for dif in difs) or all(
                    -4 < dif < 0 for dif in difs
                ):
                    result_part2 += 1
                    break
                numbers.insert(i, val)

        print(result_part1)
        print(result_part2)


if __name__ == "__main__":
    main()
