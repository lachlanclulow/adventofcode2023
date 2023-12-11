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

empty_rows = set()
empty_columns = set()

def rotate_grid(grid):
    new_grid = [[] for _ in range(len(grid[0]))]
    for row in grid:
        for i, cell in enumerate(row):
            new_grid[i].append(cell)
    return new_grid

for y, line in enumerate(example.splitlines()):
    grid.append([x for x in line])
    if '#' not in line:
        empty_rows.add(y)

grid = rotate_grid(rotate_grid(rotate_grid(grid)))
expanded_grid = []
for x, row in enumerate(grid):
    expanded_grid.append(row)
    if "#" not in row:
        empty_columns.add(x)


grid = rotate_grid(expanded_grid)


paths = {}

galaxies = []

expansion_modifier = 1_000_000

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == "#":
            galaxies.append((x, y))

for i, (x1, y1) in enumerate(galaxies[:-1]):
    for x2, y2 in galaxies[i+1:]:
        expansion = 0
        x_expansion = len(
            {x for x in range(min(x1, x2), max(x1, x2))}.intersection(empty_columns)
        )
        y_expansion = len(
            {y for y in range(min(y1, y2), max(y1, y2))}.intersection(empty_rows)
        )
        if x_expansion:
            expansion += x_expansion * (expansion_modifier - 1)
        if y_expansion:
            expansion += y_expansion * (expansion_modifier - 1)
        paths[((x1, y1),(x2, y2))] = abs(x2-x1)+abs(y2-y1) + expansion


print(sum(paths.values()))