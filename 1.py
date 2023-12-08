example = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

total = 0

digits = [
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6), 
    ("seven", 7), 
    ("eight", 8), 
    ("nine", 9)
]


for line in example.split("\n"):
    first = None
    last= None
    i = 0
    while i < len(line):
        for x, y in digits:
            if line[i:i+len(x)] == x:
                line = line[:i] + str(y) + line[i+1:]
        if line[i].isnumeric():
            if not first:
                first = line[i]
            last = line[i]
        i += 1
    total += int(first + last)

print(total)