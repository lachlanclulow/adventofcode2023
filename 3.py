example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

grid = []

symbols = []

for y, line in enumerate(example.splitlines()):
    row = []
    for x, char in enumerate(line):
        row.append(char)
        if char == "*":
            symbols.append((char, x, y))
    grid.append(row)

totals = []

for symbol, x, y in symbols:
    part_num_count = 0
    nums = []
    # right
    if x < len(grid[y]) and grid[y][x+1].isdigit():
        i = 1
        new_num = ""
        while x+i < len(grid[y]) and grid[y][x+i].isdigit():
            new_num += grid[y][x+i]
            i+=1
        nums.append(int(new_num))
    # left
    if x > 0 and grid[y][x-1].isdigit():
        i = -1
        new_num = ""
        while x+i >= 0 and grid[y][x+i].isdigit():
            new_num = grid[y][x+i] + new_num
            i-=1
        nums.append(int(new_num))
    # up
    if y > 0:
        # right
        right_num = ""
        if x < len(grid[y-1]) and grid[y-1][x+1].isdigit():
            i = 1
            right_num = ""
            while x+i < len(grid[y-1]) and grid[y-1][x+i].isdigit():
                right_num += grid[y-1][x+i]
                i+=1
        # left
        left_num = ""
        if x > 0 and grid[y-1][x-1].isdigit():
            i = -1
            while x+i >= 0 and grid[y-1][x+i].isdigit():
                left_num = grid[y-1][x+i] + left_num
                i-=1
        if grid[y-1][x].isdigit():
            nums.append(int(left_num + grid[y-1][x] + right_num))
        else:
            nums += [int('0'+left_num), int('0'+right_num)]

    # down
    if y < len(grid):
        # right
        right_num = ""
        if x < len(grid[y+1]) and grid[y+1][x+1].isdigit():
            i = 1
            right_num = ""
            while x+i < len(grid[y+1]) and grid[y+1][x+i].isdigit():
                right_num += grid[y+1][x+i]
                i+=1
        # left
        left_num = ""
        if x > 0 and grid[y+1][x-1].isdigit():
            i = -1
            while x+i >= 0 and grid[y+1][x+i].isdigit():
                left_num = grid[y+1][x+i] + left_num
                i-=1
        if grid[y+1][x].isdigit():
            nums.append(int(left_num + grid[y+1][x] + right_num))
        else:
            nums += [int('0'+left_num), int('0'+right_num)]
    no_zeros = []

    for num in nums:
        if num > 0:
            no_zeros.append(num)
    
    if len(no_zeros) == 2:
        totals.append(no_zeros[0] * no_zeros[1])

print(sum(totals))