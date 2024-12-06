def main():
    with open("input.txt", "r") as f:
        lab_map = list(map(list, map(lambda s: s.strip(), f.readlines())))
        n = len(lab_map)
        m = len(lab_map[0])

        guard_dirs_map = {
            "^": (-1, 0, ">"),
            ">": (0, 1, "v"),
            "v": (1, 0, "<"),
            "<": (0, -1, "^"),
        }
        x = 0
        y = 0
        dir = ""
        for i in range(n):
            for j in range(m):
                if lab_map[i][j] in guard_dirs_map:
                    x = i
                    y = j
                    dir = lab_map[i][j]
                    lab_map[i][j] = "."
                    break
        count = 0

        count_part2 = 0
        start_x = x
        start_y = y
        start_dir = dir

        def step(x, y, dir):
            dx, dy, next_dir = guard_dirs_map[dir]
            if lab_map[x + dx][y + dy] == "#":
                dir = next_dir
            else:
                x += dx
                y += dy
            return x, y, dir

        while x < n - 1 and x > 0 and y < m - 1 and y > 0:
            dx, dy, next_dir = guard_dirs_map[dir]
            if lab_map[x][y] == ".":
                lab_map[x][y] = "X"
                count += 1

            x, y, dir = step(x, y, dir)

        for i in range(n):
            for j in range(m):
                if lab_map[i][j] == "#" or lab_map[i][j] == ".":
                    continue
                lab_map[i][j] = "#"

                positions = set()
                x = start_x
                y = start_y
                dir = start_dir

                while x < n - 1 and x > 0 and y < m - 1 and y > 0:
                    if (x, y, dir) in positions:
                        count_part2 += 1
                        break
                    else:
                        positions.add((x, y, dir))

                    x, y, dir = step(x, y, dir)
                lab_map[i][j] = "."

        print(count + 1)
        print(count_part2)


if __name__ == "__main__":
    main()
