example = """Time:        62     64     91     90
Distance:   553   1010   1473   1074"""

example = """Time:      7  15   30
Distance:  9  40  200"""


lines = example.splitlines()

times = [int(x) for x in lines[0].split(":")[1].strip().split(" ") if x]
distances = [int(x) for x in lines[1].split(":")[1].strip().split(" ") if x]

total = 1

for i in range(len(times)):
    count = 0
    time = times[i]
    record = distances[i]
    for t in range(1, time):
        movetime = time - t
        dist = movetime * t
        if dist > record:
            count += 1
    total *= count

print(total)
