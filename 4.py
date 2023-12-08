example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

total = 0

cards = {}

import re

regex = re.compile("Card[ ]+(\d+): ")

length = len(example.splitlines())

games = []

for line in example.splitlines():
    game = int(regex.match(line).groups()[0])

    nums = line.split(":")[1].strip()
    winning_nums = [x for x in nums.split(" | ")[0].strip().split(" ")]
    my_nums = [x for x in nums.split(" | ")[1].strip().split(" ")]

    winning_set = set()
    my_num_set = set()

    for x in winning_nums:
        if x:
            winning_set.add(int(x))
    for x in my_nums:
        if x:
            my_num_set.add(int(x))
    pts = len(my_num_set.intersection(winning_set))
    games.append((game, pts, 1))

i = 0

while i < len(games):
    game, score, copies = games[i]
    for j in range(0, score):
        c_game, c_score, c_copies = games[i+j+1]
        games[i+j+1] = (c_game, c_score, c_copies+copies)

    i+=1

total = 0
for game in games:
    total += game[-1]

print(total)