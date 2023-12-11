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

rows = example.splitlines()

galaxies = []

empty_rows = {x for x in range(len(rows))}
empty_columns = {x for x in range(len(rows[0]))}

for y, line in enumerate(rows):
    for x, cell in enumerate(line):
        if cell == "#":
            galaxies.append((x, y))
            empty_rows.discard(y)
            empty_columns.discard(x)

expansion_modifier = 1_000_000 - 1

total = 0

for i, (x1, y1) in enumerate(galaxies[:-1]):
    for x2, y2 in galaxies[i+1:]:
        total += abs(x2-x1) + abs(y2-y1) + (len(
            {x for x in range(min(x1, x2)+1, max(x1, x2))}.intersection(empty_columns)
        ) + len(
            {y for y in range(min(y1, y2)+1, max(y1, y2))}.intersection(empty_rows)
        )) * expansion_modifier

print(total)