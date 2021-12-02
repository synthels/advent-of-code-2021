def part_1():
    # Part one
    horizontal_pos = 0
    depth = 0
    with open("data.txt") as file:
        lines = list(map((lambda x: x.split()), file.read().splitlines()))
        for i, j in lines:
            n = int(j)
            if i == "forward":
                horizontal_pos += n
            if i == "down":
                depth += n
            if i == "up":
                depth -= n

    print(f"part 1 solution = {horizontal_pos * depth}")


def part_2():
    # Part two
    horizontal_pos = 0
    depth = 0
    aim = 0
    with open("data.txt") as file:
        lines = list(map((lambda x: x.split()), file.read().splitlines()))
        for i, j in lines:
            n = int(j)
            if i == "forward":
                horizontal_pos += n
                depth += aim * n
            if i == "down":
                aim += n
            if i == "up":
                aim -= n

    print(f"part 2 solution = {horizontal_pos * depth}")


part_1()
part_2()
