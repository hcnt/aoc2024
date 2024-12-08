from math import gcd


def is_antinode_valid(a, n, m):
    return 0 <= a[0] < n and 0 <= a[1] < m


def calc_antinodes_part1(a: tuple[int, int], b: tuple[int, int], n, m):
    antinode1 = b[0] + b[0] - a[0], b[1] + b[1] - a[1]
    antinode2 = a[0] + a[0] - b[0], a[1] + a[1] - b[1]

    return [a for a in (antinode1, antinode2) if is_antinode_valid(a, n, m)]


def calc_antinodes_part2(a: tuple[int, int], b: tuple[int, int], n, m):
    dist_y = b[0] - a[0]
    dist_x = b[1] - a[1]
    gcd_xy = gcd(abs(dist_y), abs(dist_x))

    jump_y = dist_y // gcd_xy
    jump_x = dist_x // gcd_xy

    antinodes = []
    current_antinode = b

    while is_antinode_valid(current_antinode, n, m):
        antinodes.append(current_antinode)
        current_antinode = (current_antinode[0] + jump_y, current_antinode[1] + jump_x)

    current_antinode = a
    while is_antinode_valid(current_antinode, n, m):
        antinodes.append(current_antinode)
        current_antinode = (current_antinode[0] - jump_y, current_antinode[1] - jump_x)
    return antinodes


def main():
    with open("input2.txt", "r") as f:
        signal_map = list(map(list, map(lambda x: x.strip(), f.readlines())))
        for row in signal_map:
            print("".join(row))
        n = len(signal_map)
        m = len(signal_map[0])

        antennas = {}
        for i in range(n):
            for j in range(m):
                c = signal_map[i][j]
                if c != ".":
                    if c not in antennas:
                        antennas[c] = []
                    antennas[c].append((i, j))

        hot_spots_part1 = set()
        hot_spots_part2 = set()
        for a in antennas:
            loc_list = antennas[a]
            for i in range(len(loc_list)):
                for j in range(i + 1, len(loc_list)):
                    loc1 = loc_list[i]
                    loc2 = loc_list[j]

                    antinodes = calc_antinodes_part1(loc1, loc2, n, m)
                    for antinode in antinodes:
                        hot_spots_part1.add(antinode)

                    antinodes = calc_antinodes_part2(loc1, loc2, n, m)
                    for antinode in antinodes:
                        hot_spots_part2.add(antinode)

        print(len(hot_spots_part1))
        print(len(hot_spots_part2))


if __name__ == "__main__":
    main()
