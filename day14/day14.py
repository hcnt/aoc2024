import re
from collections import defaultdict
from operator import mul
from functools import reduce
from time import sleep


def calc_position(
    p: tuple[int, int], v: tuple[int, int], size: tuple[int, int], n: int
):
    return ((p[0] + n * v[0]) % size[0], (p[1] + n * v[1]) % size[1])


def calc_quadrant(p: tuple[int, int], size: tuple[int, int]) -> int:
    if p[0] == size[0] // 2 or p[1] == size[1] // 2:
        return -1
    return 2 * (p[0] > size[0] // 2) + (p[1] > size[1] // 2)


def print_board(positions, size):
    x, y = size
    pos = set(positions)
    for i in range(y):
        for j in range(x):
            if (j, i) in pos:
                print("*", end="")
            else:
                print(".", end="")
        print()


def generate_next_positions(positions, velocities, size):
    new_positions = [
        calc_position(p, v, size, 1) for p, v in zip(positions, velocities)
    ]
    return new_positions


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        quads = defaultdict(int)
        positions = []
        velocities = []
        for line in lines:
            g = list(
                map(int, re.findall(
                    r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)[0])
            )
            p = (g[0], g[1])
            v = (g[2], g[3])
            size = (101, 103)
            # size = (11, 7)
            positions.append(p)
            velocities.append(v)
            new_p = calc_position(p, v, size, 100)
            quads[calc_quadrant(new_p, size)] += 1

        # print_board(positions, size)
        print(quads)
        result_part1 = reduce(mul, (quads[key] for key in quads if key != -1))
        print(result_part1)

        for i in range(100000):
            quads = defaultdict(int)
            positions = generate_next_positions(positions, velocities, size)
            for pos in positions:
                quads[calc_quadrant(pos, size)] += 1
            # print(chr(27) + "[2J")
            # if 1.2 * (quads[0] + quads[2]) < quads[1] + quads[3]:
            # if (i - 3) % 103 == 0:
            print_board(positions, size)
            print(i)
            print(quads)
            sleep(1)

        # print(result_part1)


if __name__ == "__main__":
    main()
