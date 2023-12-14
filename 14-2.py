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

import numpy as np

text = example.splitlines()

def transpose(pattern):
    return ["".join(x) for x in np.rot90([list(x) for x in pattern], k=3)]

def move_rocks(s):
    return "."*s.count(".")+"O"*s.count("O")

def tilt(text):
    cycles = 4

    for _ in range(cycles):
        text = transpose(tuple(text))

        new_text = []
        for line in text:
            new_text.append("#".join([move_rocks(x) for x in line.split("#")]))
        text = new_text
    return text


arrangements = {}

loop_len = 0
offset = 0
i=0

while True:
    text = tuple(tilt(tuple(text)))
    if tuple(text) in arrangements:
        offset = arrangements[text]
        loop_len = i-offset
        break
    else:
        arrangements[text] = i
    i+=1


index = (1_000_000_000-1-offset)%(loop_len)+offset

for k, v in arrangements.items():
    if v == index:
        print(v)
        print(sum([x.count("O")*i for i, x in enumerate(reversed(k), 1)]))


