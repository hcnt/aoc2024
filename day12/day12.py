def main():
    with open("input.txt", "r") as f:
        values = [list(l.strip()) for l in f.readlines()]
        n = len(values)
        m = len(values[0])

        visited = [[False for _ in range(m)] for _ in range(n)]

        current_fences = set()

        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def count_sides():
            count = 0
            while len(current_fences) > 0:
                x, y, dir = current_fences.pop()
                di = dir % 2
                dj = 1 - (dir % 2)

                i, j = x + di, y + dj
                while (i, j, dir) in current_fences:
                    current_fences.remove((i, j, dir))
                    i += di
                    j += dj

                i, j = x - di, y - dj
                while (i, j, dir) in current_fences:
                    current_fences.remove((i, j, dir))
                    i -= di
                    j -= dj

                count += 1

            return count

        def dfs(i, j):
            if visited[i][j]:
                return 0, 0
            visited[i][j] = True
            val = values[i][j]

            plant_count = 1
            fence_count = 0

            for dindex, (di, dj) in enumerate(dirs):
                new_i = i + di
                new_j = j + dj
                if 0 <= new_i < n and 0 <= new_j < m and val == values[new_i][new_j]:
                    plants, fences = dfs(new_i, new_j)
                    plant_count += plants
                    fence_count += fences
                else:
                    fence_count += 1
                    current_fences.add((new_i, new_j, dindex))
            return plant_count, fence_count

        result_part1 = 0
        result_part2 = 0
        for i in range(n):
            for j in range(m):
                plants, fences = dfs(i, j)
                result_part1 += plants * fences
                result_part2 += plants * count_sides()

        print(result_part1)
        print(result_part2)


if __name__ == "__main__":
    main()
