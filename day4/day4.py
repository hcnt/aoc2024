def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        grid = [[c for c in line.strip()] for line in lines if line.strip()]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0]) - 3):
                if (
                    grid[i][j] == "X"
                    and grid[i][j + 1] == "M"
                    and grid[i][j + 2] == "A"
                    and grid[i][j + 3] == "S"
                ):
                    count += 1
                elif (
                    grid[i][j] == "S"
                    and grid[i][j + 1] == "A"
                    and grid[i][j + 2] == "M"
                    and grid[i][j + 3] == "X"
                ):
                    count += 1
        for i in range(len(grid[0])):
            for j in range(len(grid) - 3):
                if (
                    grid[j][i] == "X"
                    and grid[j + 1][i] == "M"
                    and grid[j + 2][i] == "A"
                    and grid[j + 3][i] == "S"
                ):
                    count += 1
                elif (
                    grid[j][i] == "S"
                    and grid[j + 1][i] == "A"
                    and grid[j + 2][i] == "M"
                    and grid[j + 3][i] == "X"
                ):
                    count += 1
        for i in range(len(grid[0]) - 3):
            for j in range(len(grid) - 3):
                if (
                    grid[j][i] == "X"
                    and grid[j + 1][i + 1] == "M"
                    and grid[j + 2][i + 2] == "A"
                    and grid[j + 3][i + 3] == "S"
                ):
                    count += 1
                elif (
                    grid[j][i] == "S"
                    and grid[j + 1][i + 1] == "A"
                    and grid[j + 2][i + 2] == "M"
                    and grid[j + 3][i + 3] == "X"
                ):
                    count += 1
        for i in range(len(grid[0]) - 3):
            for j in range(3, len(grid)):
                if (
                    grid[j][i] == "X"
                    and grid[j - 1][i + 1] == "M"
                    and grid[j - 2][i + 2] == "A"
                    and grid[j - 3][i + 3] == "S"
                ):
                    count += 1
                elif (
                    grid[j][i] == "S"
                    and grid[j - 1][i + 1] == "A"
                    and grid[j - 2][i + 2] == "M"
                    and grid[j - 3][i + 3] == "X"
                ):
                    count += 1
        print(count)
        count = 0
        # part 2
        for i in range(len(grid) - 2):
            for j in range(len(grid[i]) - 2):
                if grid[i + 1][j + 1] == "A":
                    if (
                        grid[i][j] == "M"
                        and grid[i][j + 2] == "S"
                        and grid[i + 2][j + 2] == "S"
                        and grid[i + 2][j] == "M"
                    ):
                        count += 1
                    elif (
                        grid[i][j] == "M"
                        and grid[i][j + 2] == "M"
                        and grid[i + 2][j + 2] == "S"
                        and grid[i + 2][j] == "S"
                    ):
                        count += 1
                    elif (
                        grid[i][j] == "S"
                        and grid[i][j + 2] == "M"
                        and grid[i + 2][j + 2] == "M"
                        and grid[i + 2][j] == "S"
                    ):
                        count += 1
                    elif (
                        grid[i][j] == "S"
                        and grid[i][j + 2] == "S"
                        and grid[i + 2][j + 2] == "M"
                        and grid[i + 2][j] == "M"
                    ):
                        count += 1
        print(count)


if __name__ == "__main__":
    main()
