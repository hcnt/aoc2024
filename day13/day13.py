import re


def solve(a, b, prize):
    det = a[0] * b[1] - b[0] * a[1]

    val1 = b[1] * prize[0] - b[0] * prize[1]
    val2 = a[0] * prize[1] - a[1] * prize[0]

    if val1 % det == 0 and val2 % det == 0:
        return ((val1 // det) * 3) + val2 // det

    return -1


def main():
    with open("input.txt", "r") as f:
        input = f.read()

        button_r = re.compile(
            r"^Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)$",
            re.MULTILINE,
        )
        groups = button_r.findall(input)
        sum_part1 = 0
        sum_part2 = 0
        for g in groups:
            g = list(map(int, g))
            val_part1 = solve(
                (g[0], g[1]),
                (g[2], g[3]),
                (g[4], g[5]),
            )
            val_part2 = solve(
                (g[0], g[1]),
                (g[2], g[3]),
                (g[4] + 10000000000000, g[5] + 10000000000000),
            )

            sum_part1 += val_part1 if val_part1 != -1 else 0
            sum_part2 += val_part2 if val_part2 != -1 else 0
        print(sum_part1)
        print(sum_part2)


if __name__ == "__main__":
    main()
