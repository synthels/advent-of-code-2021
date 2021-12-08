def simulate(fish, days):
    gens = [0 for i in range(9)]
    for i in fish:
        gens[i] += 1
    for day in range(days):
        parents = gens[0]
        n = 1
        while n < len(gens):
            gens[n - 1] = gens[n];
            n += 1
        gens[6] += parents
        gens[8] = parents

    return sum(gens)

def part_1():
    with open("data.txt") as file:
        fish = list(map(lambda x: int(x), [x.strip() for x in file.read().split(',')]))
        n = simulate(fish, 80)
        print(f"part 1 solution = {n}")

def part_2():
    with open("data.txt") as file:
        fish = list(map(lambda x: int(x), [x.strip() for x in file.read().split(',')]))
        n = simulate(fish, 256)
        print(f"part 2 solution = {n}")

part_1()
part_2()
