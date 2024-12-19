from functools import cache


class Trie:
    def __init__(self):
        self.is_end = False
        self.next: list[Trie | None] = [None] * 26

    def add_word(self, word: str):
        current_trie: Trie = self
        for c in word:
            c = ord(c) - ord("a")
            if current_trie.next[c] is None:
                current_trie.next[c] = Trie()
            current_trie = current_trie.next[c]
        current_trie.is_end = True

    def get_all_prefixes(self, word: str):
        current_trie: Trie = self
        for i, c in enumerate(word):
            c = ord(c) - ord("a")
            if current_trie.is_end:
                yield word[:i]
            if current_trie.next[c] is None:
                return
            current_trie = current_trie.next[c]
        if current_trie.is_end:
            yield word


def main():
    with open("input2.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

        patterns = lines[0].split(", ")
        targets = lines[2:]

        t = Trie()
        for pattern in patterns:
            t.add_word(pattern)

        @cache
        def search_part1(current_string: str):
            if current_string == "":
                return True
            return any(
                search_part1(current_string[len(pattern):])
                for pattern in t.get_all_prefixes(current_string)
            )

        print(sum(search_part1(target) for target in targets))

        @cache
        def search_part2(current_string: str):
            if current_string == "":
                return 1
            return sum(
                search_part2(current_string[len(pattern):])
                for pattern in t.get_all_prefixes(current_string)
            )

        print(sum(search_part2(target) for target in targets))


if __name__ == "__main__":
    main()
