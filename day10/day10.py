def main():
    with open("input.txt", "r") as f:
        slope_map = list(
            map(lambda x: list(map(int, x)), map(lambda x: x.strip(), f.readlines()))
        )
        n = len(slope_map)
        m = len(slope_map[0])

        result_part1 = 0
        result_part2 = 0

        visited = [[False for _ in range(m)] for _ in range(n)]

        def dfs(i, j, part1):
            if part1 and visited[i][j]:
                return 0
            visited[i][j] = True
            val = slope_map[i][j]
            if val == 9:
                return 1
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            score = 0
            for di, dj in dirs:
                if 0 <= i + di < n and 0 <= j + dj < m:
                    new_val = slope_map[i + di][j + dj]
                    if new_val == val + 1:
                        score += dfs(i + di, j + dj, part1)
            return score

        for i in range(n):
            for j in range(m):
                if slope_map[i][j] == 0:
                    visited = [[False for _ in range(m)] for _ in range(n)]
                    result_part1 += dfs(i, j, True)
                    result_part2 += dfs(i, j, False)
        print(result_part1)
        print(result_part2)


if __name__ == "__main__":
    main()
