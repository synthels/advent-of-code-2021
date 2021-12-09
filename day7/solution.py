def calc_fuel(crabs, pos, pt2):
    fuel = 0
    for c in crabs:
        n = abs(pos - c)
        if not pt2:
            fuel += n
        else:
            # Using gauss summation!
            fuel += n * (n+1) // 2
    return fuel

def get_most_efficient(crabs, pt2):
    min_fuel = float('inf')
    for i in range(max(crabs)):
        fuel = calc_fuel(crabs, i, pt2)
        min_fuel = min(min_fuel, fuel)
    return min_fuel

def part_1():
    with open("data.txt") as file:
        crabs = list(map(lambda x: int(x), [x.strip() for x in file.read().split(',')]))
        print(f"part 1 solution = {get_most_efficient(crabs, False)}")

def part_2():
    with open("data.txt") as file:
        crabs = list(map(lambda x: int(x), [x.strip() for x in file.read().split(',')]))
        print(f"part 2 solution = {get_most_efficient(crabs, True)}")

part_1()
part_2()
