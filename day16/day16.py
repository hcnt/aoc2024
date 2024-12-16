from collections import defaultdict, deque
import queue


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


def print_board(board, visited, score):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if visited[i][j]:
                print(bcolors.FAIL, end="")
            print(board[i][j], end="")
            print(bcolors.ENDC, end="")
        print()
    print(score)


dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))


def opposite_dir(dir):
    return dirs[(dirs.index(dir) + 2) % len(dirs)]


def main():
    with open("input2.txt", "r") as f:
        board = [list(line.strip()) for line in f.readlines()]
        pos = find_in_board(board, "S")
        end_pos = find_in_board(board, "E")
        dir = (0, 1)
        scores = [
            [{dir: 1 << 64 for dir in dirs} for i in range(len(board[0]))]
            for j in range(len(board))
        ]

        q = queue.PriorityQueue()
        q.put((0, pos, dir))
        scores[pos[0]][pos[1]][dir] = 0
        prev = defaultdict(list)

        while not q.empty():
            score, pos, dir = q.get()
            q.task_done()
            for d in dirs:
                new_pos = add_tuple(pos, d)
                new_y, new_x = new_pos
                if board[new_y][new_x] in (".", "E"):
                    if d == opposite_dir(dir):
                        continue
                    elif d == dir:
                        weight = 1
                    else:
                        weight = 1000

                        # reset new position because only direction changes when turning
                        new_pos = pos
                        new_y, new_x = pos[0], pos[1]

                    new_score = scores[pos[0]][pos[1]][dir] + weight
                    old_score = scores[new_y][new_x][d]
                    if old_score == new_score:
                        prev[(new_pos, d)].append((pos, dir))
                    elif new_score < old_score:
                        scores[new_y][new_x][d] = new_score
                        q.put((new_score, new_pos, d))
                        prev[(new_pos, d)].append((pos, dir))

        dir, val = min(scores[end_pos[0]][end_pos[1]
                                          ].items(), key=lambda x: x[1])
        print(val)
        dq = deque()
        dq.append((end_pos, dir))
        count = 0
        visited = [[False for i in range(len(board[0]))]
                   for j in range(len(board))]
        while dq:
            pos, dir = dq.popleft()
            pos_list = prev[(pos, dir)]
            for p, d in pos_list:
                if not visited[p[0]][p[1]]:
                    count += 1
                visited[p[0]][p[1]] = True
                dq.append((p, d))

        print(count + 1)


if __name__ == "__main__":
    main()
