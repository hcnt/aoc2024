from itertools import pairwise
from collections import deque, defaultdict


def mix(secret, num):
    return secret ^ num


assert mix(42, 15) == 37


def prune(secret):
    return secret % 16777216


assert prune(100000000) == 16113920


def next_secret(secret):
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))
    return secret


assert next_secret(123) == 15887950
assert next_secret(15887950) == 16495136


def n_th_secret(secret, n):
    for _ in range(n):
        secret = next_secret(secret)
    return secret


def prices(starting_secret):
    secret = starting_secret
    while True:
        yield secret % 10
        secret = next_secret(secret)


def price_diffs(prices_iter):
    for a, b in pairwise(prices_iter):
        yield b - a


def groupwise(iter, n):
    q = deque(maxlen=n)
    for item in iter:
        q.append(item)
        if len(q) == n:
            yield tuple(q)


def sequence_to_price_iter(starting_secret):
    consecutive_changes_iter = groupwise(
        price_diffs(prices(starting_secret)), 4)
    prices_iter = prices(starting_secret)
    for _ in range(4):
        next(prices_iter)
    return zip(consecutive_changes_iter, prices_iter)


def generate_sequence_map(starting_secret, n):
    sequence_map = {}
    for i, (seq, price) in enumerate(sequence_to_price_iter(starting_secret)):
        if i == n - 4:
            break
        if seq not in sequence_map:
            sequence_map[seq] = price
    return sequence_map


def main():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        values = [int(line) for line in lines]

        # part 1
        res_part1 = sum(n_th_secret(value, 2000) for value in values)
        print(res_part1)

        # part 2
        sequence_sums = defaultdict(int)
        for value in values:
            sequence_map = generate_sequence_map(value, 2001)
            for key in sequence_map:
                sequence_sums[key] += sequence_map[key]

        print(max(sequence_sums.items(), key=lambda a: a[1]))


if __name__ == "__main__":
    main()
