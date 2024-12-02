from collections import Counter
from pip._vendor.rich import print


def main():
    with open("input.txt", "r") as f:
        values = list(map(int, f.read().split()))
        print(values)
        first_list = values[::2]
        second_list = values[1::2]
        first_list.sort()
        second_list.sort()

        print(sum(map(lambda x: abs(x[0] - x[1]), zip(first_list, second_list))))
        c1 = Counter(first_list)
        c2 = Counter(second_list)

        print(sum(val * c2[val] for val in c1))


if __name__ == "__main__":
    main()
