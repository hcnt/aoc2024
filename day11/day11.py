from collections import defaultdict


def calc_stones(d: dict[int, int], n: int) -> int:
    for i in range(n):
        new_d = defaultdict(int)
        for key, value in d.items():
            key_str = str(key)
            if key == 0:
                new_d[1] += value
            elif len(key_str) % 2 == 0:
                new_d[int(key_str[: len(key_str) // 2])] += value
                new_d[int(key_str[len(key_str) // 2 :])] += value
            else:
                new_d[key * 2024] += value
        d = new_d
    return sum(d.values())


def main():
    with open("input.txt", "r") as f:
        values = list(map(int, f.read().strip().split(" ")))
        d = defaultdict(int)
        for value in values:
            d[value] += 1
        print(calc_stones(d, 25))
        print(calc_stones(d, 75))


if __name__ == "__main__":
    main()
