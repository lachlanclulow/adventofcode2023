example = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

grid = []

rocks = []

def tilt_rock(x, y, grid):
    i = 0
    for i in range(y, -1, -1):
        if not grid[i][x]:
            return i+1
    return i

for y, line in enumerate(example.splitlines()):
    rocks.append(0)
    grid.append([])
    for x, char in enumerate(line.strip()):
        grid[y].append(True)
        if char == "O":
            # rock
            new_y = tilt_rock(x, y, grid)
            grid[new_y][x] = False
            rocks[new_y] += 1
        elif char == "#":
            grid[y][x] = False
            
print(sum([x*i for x, i in enumerate(reversed(rocks), 1)]))