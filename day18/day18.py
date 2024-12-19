from heapq import heappush
from heapq import heappop


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def find_in_board(board, char):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == char:
                return (i, j)
    return (-1, -1)


def add_tuple(a, b):
    return tuple(map(lambda e: e[0] + e[1], zip(a, b)))


def print_board(board, visited=None):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if visited and visited[i][j]:
                print(bcolors.FAIL, end="")
            print(board[i][j], end="")
            print(bcolors.ENDC, end="")
        print()


dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))


def opposite_dir(dir):
    return dirs[(dirs.index(dir) + 2) % len(dirs)]


def dijkstra(board: list[list[str]]) -> list[list[int]]:
    n = len(board)
    m = len(board[0])
    costs = [[1 << 32 for j in range(m)] for i in range(n)]
    pq = []
    costs[0][0] = 0
    heappush(pq, (0, 0, 0))
    while pq:
        cost, y, x = heappop(pq)

        for dir in dirs:
            dy, dx = add_tuple((y, x), dir)
            if 0 <= dy < n and 0 <= dx < m and board[dy][dx] == ".":
                if costs[dy][dx] > costs[y][x] + 1:
                    costs[dy][dx] = costs[y][x] + 1
                    heappush(pq, (costs[dy][dx], dy, dx))
    return costs[-1][-1]


def main():
    with open("input2.txt", "r") as f:
        n, m = 71, 71
        values = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]

        board = [["." for j in range(m)] for i in range(n)]

        for x, y in values[:1024]:
            board[y][x] = "#"

        print(dijkstra(board))

        for x, y in values[1024:]:
            board[y][x] = "#"
            if dijkstra(board) == 1 << 32:
                print(x, y)
                break


if __name__ == "__main__":
    main()
