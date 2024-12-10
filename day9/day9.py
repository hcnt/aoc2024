def calc_checksum(disk_map):
    return sum(i * int(val) for i, val in enumerate(disk_map) if val != ".")


def main():
    with open("input.txt", "r") as f:
        values = list(map(int, f.read().strip()))

        disk_map = []
        disk_info = []
        file_id = 0
        for i in range(len(values)):
            if i % 2 == 1:
                c = "."
            else:
                c = str(file_id)
                file_id += 1
            disk_map.extend([c] * values[i])
            disk_info.append((c, values[i]))

        i = 0
        j = len(disk_map) - 1

        while i < j:
            if disk_map[i] != ".":
                i += 1
            elif disk_map[j] == ".":
                j -= 1
            else:
                disk_map[i], disk_map[j] = disk_map[j], disk_map[i]
                i += 1
                j -= 1
        print(calc_checksum(disk_map))

        moved_blocks = set()
        for i in range(len(disk_info) - 1, -1, -1):
            file_to_move = disk_info[i]
            if file_to_move[0] == "." or file_to_move[0] in moved_blocks:
                continue
            for j in range(i):
                if disk_info[j][0] == "." and disk_info[j][1] >= file_to_move[1]:
                    moved_blocks.add(disk_info[i][0])

                    space_left = disk_info[j][1] - file_to_move[1]
                    disk_info[i] = (".", file_to_move[1])
                    disk_info[j] = file_to_move

                    disk_info.insert(j + 1, (".", space_left))
                    i += 1
                    break

        disk_map = []
        for c, val in disk_info:
            disk_map.extend([c] * val)
        print(calc_checksum(disk_map))


if __name__ == "__main__":
    main()
