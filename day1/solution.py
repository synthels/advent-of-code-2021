def part_1():
    # Part one
    incr = 0
    with open("data.txt") as file:
        prev = 0
        for line in file:
            curr = int(line.rstrip())
            if curr > prev and prev != 0:
                incr += 1
            prev = curr

    print(f"part 1 solution = {incr}")


def part_2():
    # Part two
    incr = 0
    with open("data.txt") as file:
        clump = []
        prev = 0
        for line in file:
            clump.append(int(line.rstrip()))
            if len(clump) == 3:
                curr = sum(clump)
                if curr > prev and prev != 0:
                    incr += 1
                clump.pop(0)
                prev = curr

    print(f"part 1 solution = {incr}")


part_1()
part_2()
