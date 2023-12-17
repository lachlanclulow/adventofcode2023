example = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

example = """111111111111
999999999991
999999999991
999999999991
999999999991"""


import heapq

INF = float("inf")

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

valid_dirs = {
    UP: {UP, LEFT, RIGHT},
    DOWN: {DOWN, LEFT, RIGHT},
    LEFT: {LEFT, UP, DOWN},
    RIGHT: {RIGHT, UP, DOWN}
}

vertices = {}

grid = []

height = len(example.splitlines())
width = len(example.splitlines()[0])

for line in example.splitlines():
    grid.append([int(x) for x in line.strip()])


explored = set()
start_cost = 0
start_pos = (0, 0)
target = (width-1, height-1)

q = [(start_cost, start_pos, DOWN, 1), (start_cost, start_pos, RIGHT, 1)]

def add_tuple(a, b):
    return (a[0]+b[0],a[1]+b[1])

def is_valid_step(v, line_len):
    x, y = v    
    if (x < 0 or x > width-1 or y < 0 or y > height-1) or \
        line_len > 10:
        return False
    return True


while len(q):
    cost, u, direction, line_len = heapq.heappop(q)
    if (u, direction, line_len) not in explored:
        explored.add((u, direction, line_len))
        x, y = v = add_tuple(u, direction)
        
        if is_valid_step(v, line_len):
            cost += grid[y][x]

            # Reached the end
            if v == target and line_len >= 4:
                print(cost)
                break
            
            for new_direction in valid_dirs[direction]:
                new_line_len = line_len
                if new_direction == direction:
                    new_line_len += 1
                else:
                    new_line_len = 1
                if (new_direction == direction and new_line_len <=10) or line_len >= 4:
                    heapq.heappush(q, (cost, v, new_direction, new_line_len))








