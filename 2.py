import re

example = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

cubes = {
    "red": 0,
    "green": 0,
    "blue": 0
}

regex = re.compile("Game (\d+): (.*)")
cuberegex = re.compile("(\d+) ([a-z]+)")

total = 0

for line in example.split('\n'):
    groups = regex.match(line).groups()

    game = int(groups[0])
    
    sets = {}
    for set in groups[1].split("; "):
        #sets = {}
        for cube in set.split(", "):
            #print(cube)
            match = cuberegex.match(cube).groups()
            num = match[0]
            color = match[1]
            sets[color] = max(int(num), sets[color] if color in sets else 0)
            # if color in sets:
            #     sets[color] = max(int(num)
            # else:
            #     sets[color] = int(num)
    #print(sets)
    power = 1
    for k, v in sets.items():
        power *= v
    #print(power)
    total += power
    #total += game

#print(cubes)

print(total)