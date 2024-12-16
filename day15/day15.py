from copy import deepcopy

dirs = {"<": (0, -1), ">": (0, 1), "v": (1, 0), "^": (-1, 0)}


def find_in_board(board, char):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == char:
                return (i, j)
    return (-1, -1)


def add_tuple(a, b):
    return tuple(map(lambda e: e[0] + e[1], zip(a, b)))


def print_board(board):
    for i in range(len(board)):
        print("".join(board[i]))


def count_boxes(board, char):
    s = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == char:
                s += 100 * i + j
    return s


def step(board, pos: tuple[int, int], move: tuple[int, int]):
    y, x = pos
    new_y, new_x = add_tuple(pos, move)
    match board[new_y][new_x]:
        case "#":
            return pos
        case ".":
            board[new_y][new_x] = "@"
            board[y][x] = "."
            return new_y, new_x
        case "O":
            i, j = new_y, new_x
            while board[i][j] == "O":
                i, j = add_tuple((i, j), move)
            if board[i][j] == "#":
                return pos
            elif board[i][j] == ".":
                board[i][j] = "O"
                board[y][x] = "."
                board[new_y][new_x] = "@"
                return new_y, new_x


def move_boxes_horizontally(board, pos, move):
    i, j = pos
    while board[i][j] in ("[", "]"):
        last_char = board[i][j]
        board[i][j] = "[" if board[i][j] == "]" else "]"
        i, j = add_tuple((i, j), move)
    board[i][j] = last_char


def check_vertical_move(board, pos, move):
    y1, x1 = pos
    if board[y1][x1] == ".":
        return True
    if board[y1][x1] == "#":
        return False

    y2, x2 = y1, (x1 - 1 if board[y1][x1] == "]" else x1 + 1)

    new_pos1 = add_tuple(pos, move)
    new_pos2 = add_tuple((y2, x2), move)

    return check_vertical_move(board, new_pos1, move) and check_vertical_move(
        board, new_pos2, move
    )


def move_boxes_vertically(board, pos, move, moved_positions):
    if pos in moved_positions:
        return

    y1, x1 = pos
    y2, x2 = y1, (x1 - 1 if board[y1][x1] == "]" else x1 + 1)

    new_y1, new_x1 = add_tuple(pos, move)
    new_y2, new_x2 = add_tuple((y2, x2), move)

    if board[new_y1][new_x1] != ".":
        move_boxes_vertically(board, (new_y1, new_x1), move, moved_positions)
    if board[new_y2][new_x2] != ".":
        move_boxes_vertically(board, (new_y2, new_x2), move, moved_positions)

    board[new_y1][new_x1] = board[y1][x1]
    board[new_y2][new_x2] = board[y2][x2]

    board[y1][x1] = "."
    board[y2][x2] = "."

    moved_positions.add((y1, x1))
    moved_positions.add((y2, x2))


def find_horizontal_box_end(board, pos, move):
    i, j = pos
    while board[i][j] in ("[", "]"):
        i, j = add_tuple((i, j), move)
    return i, j


def step2(board, pos: tuple[int, int], move: tuple[int, int]):
    y, x = pos
    new_pos = add_tuple(pos, move)
    new_y, new_x = new_pos
    match board[new_y][new_x]:
        case "#":
            return pos
        case ".":
            board[new_y][new_x] = "@"
            board[y][x] = "."
            return new_pos
        case "[" | "]":
            if move[1] != 0:  # only horizontal moves
                i, j = find_horizontal_box_end(board, new_pos, move)
                if board[i][j] == "#":
                    return pos
                elif board[i][j] == ".":
                    move_boxes_horizontally(board, new_pos, move)
                    board[new_y][new_x] = "@"
                    board[y][x] = "."
                    return new_pos
            elif move[0] != 0:  # only vertical moves
                if check_vertical_move(board, new_pos, move):
                    move_boxes_vertically(board, new_pos, move, set())
                    board[new_y][new_x] = "@"
                    board[y][x] = "."
                    return new_pos
                else:
                    return pos


def scale_board(board):
    mapping = {".": [".", "."], "#": ["#", "#"],
               "@": ["@", "."], "O": ["[", "]"]}
    new_board = [[]]
    for line in board:
        for char in line:
            new_board[-1].extend(mapping[char])
        new_board.append([])
    return new_board


def main():
    with open("input2.txt", "r") as f:
        values = f.readlines()
        moves = []
        while (line := values.pop()) != "\n":
            moves.append(line.strip())
        moves = "".join(reversed(moves))
        starting_warehouse = [list(line.strip()) for line in values]

        # part 1
        warehouse = deepcopy(starting_warehouse)

        y, x = find_in_board(warehouse, "@")
        for move in moves:
            y, x = step(warehouse, (y, x), dirs[move])

        print(count_boxes(warehouse, "O"))

        # part2
        warehouse = scale_board(starting_warehouse)

        y, x = find_in_board(warehouse, "@")
        for move in moves:
            y, x = step2(warehouse, (y, x), dirs[move])

        print(count_boxes(warehouse, "["))


if __name__ == "__main__":
    main()
