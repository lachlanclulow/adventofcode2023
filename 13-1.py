example = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

# example = """......
# #.....
# ##....
# ###...
# ####..
# #####.
# #####.

# ......
# .#....
# #....#
# ##....
# ##....
# ......
# ......"""

import numpy as np

def get_patterns(example):
    pattern = []
    for line in example.splitlines():
        if line == "":
            yield pattern
            pattern = []
        else:
            pattern.append(tuple([x for x in line.strip()]))
        
    yield pattern

def get_reflection(pattern):
    for i in range(1, len(pattern)):
        fold_a, fold_b = (pattern[i-1::-1], pattern[i:])
        fold_len = min(len(fold_a), len(fold_b))
        fold_a = tuple(fold_a[:fold_len])
        fold_b = tuple(fold_b[:fold_len])

        if hash(fold_a) == hash(fold_b):
            return i
    
    return 0


        
def transpose(pattern):
    return [tuple(x) for x in np.transpose(pattern)]

total = 0

for pattern in get_patterns(example):
    row_refl = get_reflection(pattern) * 100
    column_refl = get_reflection(transpose(pattern))

    total += max(row_refl, column_refl)

print(total)
