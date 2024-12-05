from itertools import pairwise
from functools import cmp_to_key


def main():
    with open("input.txt", "r") as f:
        values = list(map(lambda line: line.strip(), f.readlines()))
        pairs = set()

        count_part1 = 0
        count_part2 = 0

        i = 0
        while values[i] != "":
            pairs.add(tuple(map(int, reversed(values[i].split("|")))))
            i += 1

        i += 1

        def is_less(a: int, b: int) -> bool:
            return -1 if (b, a) in pairs else 1

        while values[i] != "":
            numbers = list(map(int, values[i].split(",")))
            middle_number = numbers[len(numbers) // 2]
            is_valid = True
            for pair in pairwise(numbers):
                if pair in pairs:
                    is_valid = False
                    break
            count_part1 += is_valid * middle_number

            sorted_numbers = sorted(numbers, key=cmp_to_key(is_less))
            sorted_middle_number = sorted_numbers[len(sorted_numbers) // 2]

            count_part2 += (not is_valid) * sorted_middle_number

            i += 1

        print(count_part1)
        print(count_part2)


if __name__ == "__main__":
    main()
