import math

example = """Time:        62649190
Distance:   553101014731074"""

# example = """Time:      71530
# Distance:  940200"""

def find_roots(a, b, c):
    dis_form = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis_form)) 

    return sorted(tuple([(-b + sqrt_val) / (2 * a), (-b - sqrt_val) / (2 * a)]))

lines = example.splitlines()

times = [int(x) for x in lines[0].split(":")[1].strip().split(" ") if x]
distances = [int(x) for x in lines[1].split(":")[1].strip().split(" ") if x]

total = 1

for i in range(len(times)):
    count = 0
    time = times[i]
    record = distances[i]

    a, b = find_roots(1, time, record)
    print(abs(math.floor(a) - math.floor(b)))
