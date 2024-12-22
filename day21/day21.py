from functools import cache
from itertools import pairwise, product

numeric_keypad = {
    "A": (0, 0),
    "0": (1, 0),
    "3": (0, 1),
    "2": (1, 1),
    "1": (2, 1),
    "6": (0, 2),
    "5": (1, 2),
    "4": (2, 2),
    "9": (0, 3),
    "8": (1, 3),
    "7": (2, 3),
}
directional_keypad = {
    "A": (0, 1),
    "^": (1, 1),
    ">": (0, 0),
    "v": (1, 0),
    "<": (2, 0),
}

dirs = {
    "^": (0, 1),
    ">": (-1, 0),
    "v": (0, -1),
    "<": (1, 0),
}


def add_tuple(a, b):
    return tuple(map(lambda e: e[0] + e[1], zip(a, b)))


Moves = tuple[tuple[str, int], tuple[str, int]]


@cache
def coords_diff_to_moves(coords_diff) -> Moves:
    if coords_diff[0] > 0:
        move_horizontal = "<"
    elif coords_diff[0] < 0:
        move_horizontal = ">"
    else:
        move_horizontal = ""

    if coords_diff[1] > 0:
        move_vertical = "^"
    elif coords_diff[1] < 0:
        move_vertical = "v"
    else:
        move_vertical = ""

    moves = (
        (move_horizontal, abs(coords_diff[0])),
        (move_vertical, abs(coords_diff[1])),
    )
    return moves


@cache
def generate_possible_paths(
    start_coord: tuple[int, int], moves: Moves, banned_coord: tuple[int, int]
):
    result = []
    moves = list(map(list, moves))

    def gen(current_path, current_coord):
        if all(count == 0 for move, count in moves):
            result.append(current_path + "A")
        if current_coord == banned_coord:
            return
        for i, move in enumerate(moves):
            dir, count = move
            if count > 0:
                moves[i][1] -= 1
                gen(current_path + dir, add_tuple(current_coord, dirs[dir]))
                moves[i][1] += 1

    gen("", start_coord)

    return result


@cache
def moves_for_coords(source_coord, target_coord, banned_coord):
    coords_diff = (
        target_coord[0] - source_coord[0],
        target_coord[1] - source_coord[1],
    )
    moves = coords_diff_to_moves(coords_diff)
    return generate_possible_paths(source_coord, moves, banned_coord)


@cache
def numeric_keypad_moves(source_key, target_key):
    source_key_coords = numeric_keypad[source_key]
    target_key_coords = numeric_keypad[target_key]

    return moves_for_coords(source_key_coords, target_key_coords, (2, 0))


@cache
def directional_keypad_moves(source_key, target_key):
    source_key_coords = directional_keypad[source_key]
    target_key_coords = directional_keypad[target_key]

    return moves_for_coords(source_key_coords, target_key_coords, (2, 1))


def gen_moves_for_numeric(code):
    code = "A" + code
    moves = [""]
    new_moves = []
    for a, b in pairwise(code):
        new_moves = [a[0] + a[1]
                     for a in product(moves, numeric_keypad_moves(a, b))]
        moves = new_moves
    return moves


@cache
def shortest_directional_code_length(code, i):
    code = "A" + code
    length = 0
    for a, b in pairwise(code):
        if i == 1:
            length += len(min(directional_keypad_moves(a, b), key=len))
        else:
            possible_moves = directional_keypad_moves(a, b)
            length += min(
                shortest_directional_code_length(move, i - 1) for move in possible_moves
            )
    return length


def shortest_code_length(code, directional_robots):
    directional_codes = gen_moves_for_numeric(code)

    return min(
        shortest_directional_code_length(code, directional_robots)
        for code in directional_codes
    )


def solve(codes, directional_robots):
    return sum(
        (shortest_code_length(code, directional_robots) * int(code[:-1]))
        for code in codes
    )


def main():
    with open("input.txt", "r") as f:
        codes = [line.strip() for line in f.readlines()]
        print(solve(codes, 2))
        print(solve(codes, 25))


if __name__ == "__main__":
    main()
