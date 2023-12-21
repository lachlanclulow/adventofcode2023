example = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""

rocks = set()

start = None


grid = []
for y, line in enumerate(example.splitlines()):
    row = []
    for x, c in enumerate(line):
        if c == "#":
            rocks.add((x, y))
        if c == "S":
            start = (x, y)
        row.append(c)
    grid.append(row)

height = len(example.splitlines())
width = len(example.splitlines()[0])

UP=(0, -1)
DOWN=(0, 1)
LEFT=(-1, 0)
RIGHT=(1, 0)

def f_n(n, start):
    steps = {start}
    for i in range(n):
        new_steps = set()
        for step in steps:
            new_steps |= {(step[0]+x[0], step[1]+x[1]) for x in [UP, DOWN, LEFT, RIGHT] if ((step[0]+x[0]) % width, (step[1]+x[1]) % height) not in rocks}
        steps = new_steps
    return len(steps)

print(f"Part 1: {f_n(64, start)}")

a = (f_n(65, start), f_n(65 + width, start), f_n(65 + 2*width, start))

goal = 26501365
def interpolate(n, *a):
    a0, a1, a2 = a

    b0 = a0
    b1 = a1-a0
    b2 = a2-a1
    return b0 + b1*n + (n*(n-1)//2)*(b2-b1)

print(f"Part 2: {interpolate(goal//width, *a)}")
