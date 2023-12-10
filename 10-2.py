example = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

example = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

example =  """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

example = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

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
shapes = {}

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
            shapes[(x, y)] = char

steps = 1
last = start
curr = None

for d in [NORTH, SOUTH, EAST, WEST]:
    adjacent = tuple([sum(x) for x in zip(start, d)])
    if adjacent in pipes:
        for connection in pipes[adjacent]:
            if connection == start:
                curr = adjacent
                break
    if curr:
        break

loop = [curr]
last_dir = tuple([sum(x) for x in zip(curr, (-start[0], -start[1]))])
right_turns = 0
left = set()
right = set()

while curr != start:
    dir = tuple([sum(x) for x in zip(curr, (-last[0], -last[1]))])
    if (last_dir, dir) in {
        (NORTH, EAST), (EAST, SOUTH), (SOUTH, WEST)
    }:
        right_turns += 1
    elif (last_dir, dir) in {
        (NORTH, WEST), (WEST, SOUTH), (SOUTH, EAST)
    }:
        right_turns -= 1
    
    if (shapes[curr] in {'|', 'F', '7'}) and dir == NORTH:
        left.add(tuple([sum(x) for x in zip(curr, WEST)]))
        right.add(tuple([sum(x) for x in zip(curr, EAST)]))
        if shapes[curr] == 'F':
            left.add(tuple([sum(x) for x in zip(curr, NORTH)]))
            right.add(tuple([sum(x) for x in zip(curr, SOUTH)]))
        if shapes[curr] == '7':
            left.add(tuple([sum(x) for x in zip(curr, SOUTH)]))
            right.add(tuple([sum(x) for x in zip(curr, NORTH)]))

    if (shapes[curr] in {'|', 'J', 'L'}) and dir == SOUTH:
        right.add(tuple([sum(x) for x in zip(curr, WEST)]))
        left.add(tuple([sum(x) for x in zip(curr, EAST)]))
        if shapes[curr] == 'J':
            left.add(tuple([sum(x) for x in zip(curr, SOUTH)]))
            right.add(tuple([sum(x) for x in zip(curr, NORTH)]))
        elif shapes[curr] == 'L':
            left.add(tuple([sum(x) for x in zip(curr, NORTH)]))
            right.add(tuple([sum(x) for x in zip(curr, SOUTH)]))
    if (shapes[curr] in {'-', 'J', '7'}) and dir == EAST:
        left.add(tuple([sum(x) for x in zip(curr, NORTH)]))
        right.add(tuple([sum(x) for x in zip(curr, SOUTH)]))
        if shapes[curr] == 'J':
            right.add(tuple([sum(x) for x in zip(curr, EAST)]))
            left.add(tuple([sum(x) for x in zip(curr, WEST)]))
        if shapes[curr] == '7':
            right.add(tuple([sum(x) for x in zip(curr, WEST)]))
            left.add(tuple([sum(x) for x in zip(curr, EAST)]))
    if (shapes[curr] in {'-', 'F', 'L'}) and dir == WEST:
        right.add(tuple([sum(x) for x in zip(curr, NORTH)]))
        left.add(tuple([sum(x) for x in zip(curr, SOUTH)]))
        if shapes[curr] in 'F':
            left.add(tuple([sum(x) for x in zip(curr, EAST)]))
            right.add(tuple([sum(x) for x in zip(curr, WEST)]))
        if shapes[curr] in 'L':
            left.add(tuple([sum(x) for x in zip(curr, WEST)]))
            right.add(tuple([sum(x) for x in zip(curr, EAST)]))

    tmp = curr
    curr = list(pipes[curr].difference({last}))[0]
    last = tmp
    steps += 1
    loop.append(curr)

    last_dir = dir

in_loop = set()
loop_set = set(loop)
out_loop = set(loop)

if right_turns > 0:
    # clockwise
    in_loop=right - out_loop
else:
    # anticlockwise
    in_loop=left - out_loop


i = 0
in_loop_list = list(in_loop)
while i < len(in_loop):
    x, y = in_loop_list[i]
    if (x, y) == (46, 86):
        print("im here")
    for d in [NORTH, SOUTH, EAST, WEST]:
        adj = tuple([sum(x) for x in zip((x, y), d)])
        if adj not in out_loop and adj not in in_loop:
            in_loop_list.append(adj)
            in_loop.add(adj)
    i += 1

print(len(in_loop))
