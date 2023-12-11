import json

example = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

grid = []

def rotate_grid(grid):
    new_grid = [[] for _ in range(len(grid[0]))]
    for row in grid:
        for i, cell in enumerate(row):
            new_grid[i].append(cell)
    return new_grid

for line in example.splitlines():
    grid.append([x for x in line])
    if '#' not in line:
        grid.append([x for x in line])

grid = rotate_grid(grid)
expanded_grid = []
for row in grid:
    expanded_grid.append(row)
    if "#" not in row:
        expanded_grid.append(row)

grid = rotate_grid(expanded_grid)

paths = {}

galaxies = []

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == "#":
            galaxies.append((x, y))

for i, (x1, y1) in enumerate(galaxies[:-1]):
    for x2, y2 in galaxies[i+1:]:
        paths[((x1, y1),(x2, y2))] = abs(x2-x1)+abs(y2-y1)

print(paths)

print(sum(paths.values()))