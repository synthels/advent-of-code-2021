GRID_LENGTH = 1000

def place_point(grid, x, y):
    grid[y][x] += 1


def draw_line(grid, x1, y1, x2, y2, diags):
    xs = sorted((x1, x2))
    ys = sorted((y1, y2))
    if x1 == x2:
        for y in range(ys[0], ys[1] + 1):
            place_point(grid, x1, y)
    elif y1 == y2:
        for x in range(xs[0], xs[1] + 1):
            place_point(grid, x, y1)
    elif diags:
        ix = ((x2 - x1) // abs(x2 - x1))
        iy = ((y2 - y1) // abs(y2 - y1))
        for i in range(abs(x1 - x2) + 1):
            place_point(grid, x1 + i * ix, y1 + i * iy)

def part_1():
    grid = [[0 for i in range(GRID_LENGTH)] for i in range(GRID_LENGTH)]
    inter = 0
    with open("data.txt") as file:
        lines = list(map((lambda x: x.split()),
                     file.read().splitlines()))
        # Draw lines
        for line in lines:
            line.pop(1)
            l1 = line[0].split(',')
            l2 = line[1].split(',')
            draw_line(grid, int(l1[0]), int(l1[1]), int(l2[0]), int(l2[1]), False)
        for row in grid:
            for i in row:
                if i >= 2:
                    inter += 1

        print(f"part 1 solution = {inter}")

def part_2():
    grid = [[0 for i in range(GRID_LENGTH)] for i in range(GRID_LENGTH)]
    inter = 0
    with open("data.txt") as file:
        lines = list(map((lambda x: x.split()),
                    file.read().splitlines()))
        # Draw lines
        for line in lines:
            line.pop(1)
            l1 = line[0].split(',')
            l2 = line[1].split(',')
            draw_line(grid, int(l1[0]), int(l1[1]), int(l2[0]), int(l2[1]), True)
        for row in grid:
            for i in row:
                if i >= 2:
                    inter += 1
        print(f"part 2 solution = {inter}")

part_1()
part_2()
