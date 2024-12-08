def backtrack(test, values, i, current, part2):
    if current > test:
        return False
    if i == len(values):
        return current == test
    if backtrack(test, values, i + 1, current + values[i], part2):
        return True
    if backtrack(test, values, i + 1, current * values[i], part2):
        return True
    if part2 and backtrack(
        test, values, i + 1, int(str(current) + str(values[i])), part2
    ):
        return True
    return False


def solve(test, values, part2):
    return backtrack(test, values, 1, values[0], part2)


def main():
    with open("input2.txt", "r") as f:
        lines = f.readlines()
        result_part1 = 0
        result_part2 = 0
        for line in lines:
            test, values = line.strip().split(":")
            test = int(test)
            values = list(map(int, values.strip().split(" ")))
            if solve(test, values, False):
                result_part1 += test
                result_part2 += test
            elif solve(test, values, True):
                result_part2 += test

        print(result_part1)
        print(result_part2)


if __name__ == "__main__":
    main()
