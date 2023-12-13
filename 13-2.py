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
            yield tuple(pattern)
            pattern = []
        else:
            pattern.append(tuple([x for x in line.strip()]))
        
    yield tuple(pattern)

def get_reflection(pattern):
    for i in range(1, len(pattern)):
        fold_a, fold_b = (pattern[i-1::-1], pattern[i:])
        fold_len = min(len(fold_a), len(fold_b))
        fold_a = fold_a[:fold_len]
        fold_b = fold_b[:fold_len]

        if fold_a == fold_b:
            return i
    
    return 0

def get_reflection_1_diff(pattern):
    for i in range(1, len(pattern)):
        fold_a, fold_b = (pattern[i-1::-1], pattern[i:])
        diffs = 0
        for a, b in zip(fold_a, fold_b):
            for x, y in zip(a, b):
                if x != y:
                    diffs += 1
                if diffs > 1:
                    break
            if diffs > 1:
                break
        if diffs == 1:
            return i

    return 0

def transpose(pattern):
    return tuple([tuple(x) for x in np.transpose(pattern)])

total = 0

for pattern in get_patterns(example):
    row_refl = get_reflection_1_diff(pattern) * 100
    column_refl = get_reflection_1_diff(transpose(pattern))
    total += max(row_refl, column_refl)


print(total)
