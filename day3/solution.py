def invert(bstr):
    """
    Inverts "binary" string
    """
    nstr = ""
    for i in bstr:
        nstr += '1' if i == '0' else '0'
    return nstr


def filter_out(binary, most_common):
    """
    Filter out values
    """
    for i in range(len(binary[0])):
        ones = 0
        zeros = 0
        for bits in binary:
            bit = bits[i]
            if bit == '1':
                ones += 1
            if bit == '0':
                zeros += 1
        if most_common:
            sig = '1' if ones >= zeros else '0'
        else:
            sig = '0' if zeros <= ones else '1'
        binary = list(filter(lambda x: x[i] == sig, binary))
        if len(binary) == 1:
            break

    return ''.join(map(str, [y for x in binary for y in x]))


def part_1():
    # Part one
    epsilon = ''
    gamma = ''
    with open("data.txt") as file:
        binary = [list(i) for i in file.read().splitlines()]
        for i in range(len(binary[0])):
            ones = 0
            zeros = 0
            for bits in binary:
                bit = bits[i]
                if bit == '1':
                    ones += 1
                else:
                    zeros += 1
            epsilon += '1' if ones > zeros else '0'
            gamma = invert(epsilon)

    print(f"part 1 solution = {int(epsilon, 2) * int(gamma, 2)}")


def part_2():
    # Part two
    with open("data.txt") as file:
        binary = [list(i) for i in file.read().splitlines()]
        print(
            f"part 2 solution = {int(filter_out(binary, True), 2) * int(filter_out(binary, False), 2)}")


part_1()
part_2()
