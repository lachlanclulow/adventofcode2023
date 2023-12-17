import sys
sys.setrecursionlimit(10000)

grid = []

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

with open("16.txt", "r") as fd:
    for line in fd.readlines():
        grid.append(tuple([x for x in line.strip()]))

height = len(grid)
width = len(grid[0])

def add(a, b):
    return tuple([sum(x) for x in zip(a, b)])

cell_map = {
    '/': {
        RIGHT:UP,
        LEFT:DOWN,
        UP:RIGHT,
        DOWN:LEFT
    },
    '\\':
    {
        RIGHT:DOWN,
        LEFT:UP,
        UP:LEFT,
        DOWN:RIGHT 
    }
}

def traverse(dir, pos, visited=set(), visited_w_dir=set()):
    global grid
    global height
    global width
    if (pos[0] < 0 or pos[0] >= width or pos[1] < 0 or pos[1] >= height) or (pos, dir) in visited_w_dir:
        return visited
    visited_w_dir.add((pos, dir))
    visited.add(pos)
    cell = grid[pos[1]][pos[0]]

    if cell == '|':
        if dir in [LEFT, RIGHT]:
            return traverse(UP, add(pos, UP), visited, visited_w_dir).union(
                traverse(DOWN, add(pos, DOWN), visited, visited_w_dir)
            )
    elif cell == '-':
        if dir in [UP, DOWN]:
            return traverse(LEFT, add(pos, LEFT), visited, visited_w_dir).union(
                traverse(RIGHT, add(pos, RIGHT), visited, visited_w_dir)
            )
    # elif cell == '/':
    #     if dir == RIGHT:
    #         dir = UP
    #     elif dir == LEFT:
    #         dir = DOWN
    #     elif dir == UP:
    #         dir = RIGHT
    #     elif dir == DOWN:
    #         dir = LEFT
    
    # elif cell == '\\':
    #     if dir == RIGHT:
    #         dir = DOWN
    #     elif dir == LEFT:
    #         dir = UP
    #     elif dir == UP:
    #         dir = LEFT
    #     elif dir == DOWN:
    #         dir = RIGHT
    if cell in cell_map:
        dir = cell_map[cell][dir]
    
    return traverse(dir, add(pos, dir), visited, visited_w_dir)

start_pos = [(DOWN, (x, 0)) for x in range(width)] +\
    [(UP, (x, height-1)) for x in range(width)] +\
    [(RIGHT, (y, 0)) for y in range(height)] +\
    [(LEFT, (y, width-1)) for y in range(height)]

print(f"part 1: {len(traverse(RIGHT, (0, 0)))}")

print(f"part 2: {max([len(traverse(dir, pos, set(), set())) for dir, pos in start_pos])}")
