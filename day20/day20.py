from collections import deque
from copy import deepcopy


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
            # if board[i][j] == "#":
            #     print("##", end="")
            # else:
            #     print(f"{board[i][j]:02}", end="")
            print(board[i][j], end="")
            print(bcolors.ENDC, end="")
        print()


dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))


def opposite_dir(dir):
    return dirs[(dirs.index(dir) + 2) % len(dirs)]


def gen_visited(board):
    return [[False for _ in range(len(board[i]))] for i in range(len(board))]


def calulate_costs(board, start):
    visited = gen_visited(board)
    cost_board = deepcopy(board)
    q = deque()
    q.append((start, 0))

    while q:
        pos, dist = q.popleft()
        y, x = pos
        if visited[y][x]:
            continue
        visited[y][x] = True
        cost_board[y][x] = dist
        for dir in dirs:
            new_pos = add_tuple(pos, dir)
            new_y, new_x = new_pos
            if board[new_y][new_x] != "#":
                q.append((new_pos, dist + 1))
    return cost_board


def get_surrounding_values(board, pos, max_dist):
    counts = []
    visited = set()
    q = deque()
    q.append((pos, 0))
    while q:
        pos, dist = q.popleft()
        y, x = pos
        if pos in visited:
            continue
        visited.add(pos)
        if dist > max_dist:
            continue
        if board[y][x] != "#":
            counts.append((board[y][x], dist))
        for dir in dirs:
            new_pos = add_tuple(pos, dir)
            new_y, new_x = new_pos
            if 0 <= new_y < len(board) and 0 <= new_x < len(board[new_y]):
                q.append((new_pos, dist + 1))

    return counts


def count_cheats(cost_board, board, start, max_cheat_dist, min_cost_saving):
    visited = gen_visited(board)

    s = []
    s.append(start)

    counts = 0
    while s:
        pos = s.pop()
        y, x = pos
        current_cost = cost_board[y][x]
        if visited[y][x]:
            continue
        visited[y][x] = True
        if board[y][x] == "E":
            continue

        surrounding_costs = get_surrounding_values(
            cost_board, pos, max_cheat_dist)
        diffs = [
            current_cost - (c + dist)
            for c, dist in surrounding_costs
            if current_cost - (c + dist) >= min_cost_saving
        ]
        counts += len(diffs)

        for dir in dirs:
            new_pos = add_tuple(pos, dir)
            new_y, new_x = new_pos
            if board[new_y][new_x] != "#":
                s.append(new_pos)
    return counts


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

        board = [list(line.strip()) for line in lines]
        start = find_in_board(board, "S")
        end = find_in_board(board, "E")

        cost_board = calulate_costs(board, end)

        print(count_cheats(cost_board, board, start, 2, 100))
        print(count_cheats(cost_board, board, start, 20, 100))


if __name__ == "__main__":
    main()
