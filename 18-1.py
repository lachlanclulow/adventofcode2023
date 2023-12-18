example = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

import numpy as np

min_x = 0
max_x = 0
min_y = 0
max_y = 0

dirs = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0)
}

curr_coords = (0, 0)
curr_corner = (0, 0)
corners = [(0, 0)]

coords = set()
coords_list = []

perimeter = 0

for line in example.splitlines():
    direction, num, colour = line.split()
    num = int(num)
    perimeter += num
    colour = colour.strip("()")
    x, y = curr_coords
    dx, dy = dirs[direction]
    x += dx*num
    y += dy*num
    curr_coords = (x, y)
    coords_list.append(curr_coords)


# copy pasted this badboy from here https://stackoverflow.com/a/58515054
def shoelace(x_y):
    x_y = np.array(x_y)
    x_y = x_y.reshape(-1,2)

    x = x_y[:,0]
    y = x_y[:,1]

    S1 = np.sum(x*np.roll(y,-1))
    S2 = np.sum(y*np.roll(x,-1))

    area = .5*np.absolute(S1 - S2)

    return area

area = shoelace(coords_list)

print(int(area - perimeter/2+1 + perimeter))
