example = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

dirs = {
    "L": 0,
    "R": 1
}

lines = example.splitlines()

instructions = [dirs[x] for x in lines[0].strip()]

start_nodes = []

nodes = {}

for line in lines[2:]:
    node, paths = line.split(" = ")
    nodes[node] = tuple(paths[1:-1].split(", "))
    if node[-1] == 'A':
        start_nodes.append(node)

import math

lengths = []

for node in start_nodes:
    i = 0
    while node[-1] != 'Z':
        node = nodes[node][instructions[i % len(instructions)]]
        i+=1
    lengths.append(i)

print(math.lcm(*lengths))
