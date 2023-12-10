example = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)

pipe_types = {
    "|": (NORTH, SOUTH),
    "-": (EAST, WEST),
    "L": (NORTH, EAST),
    "J": (WEST, NORTH),
    "7": (WEST, SOUTH),
    "F": (SOUTH, EAST),
    ".": ()
}

start = None

pipes = {}

width = 0
height = 0

for y, line in enumerate(example.splitlines()):
    height = y+1
    for x, char in enumerate(line):
        width = x+1
        if char == 'S':
            start = (x, y)
        else:
            dirs = pipe_types[char]
            pipes[(x, y)] = {
                tuple(
                    [sum(j) for j in zip(i, (x, y))]
                ) for i in dirs
            }

connected = []

for d in [NORTH, SOUTH, EAST, WEST]:
    adjacent = tuple([sum(x) for x in zip(start, d)])
    if adjacent in pipes:
        for connection in pipes[adjacent]:
            if connection == start:
                connected.append(adjacent)

steps = 1
last = start
curr = connected[0]
while curr != start:
    tmp = curr
    curr = list(pipes[curr].difference({last}))[0]
    last = tmp
    steps += 1

print(steps/2)