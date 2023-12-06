import math

example = """Time:        62649190
Distance:   553101014731074"""

# example = """Time:      71530
# Distance:  940200"""

def find_roots(a, b, c):
    dis_form = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis_form)) 

    return tuple([(-b + sqrt_val) / (2 * a), (-b - sqrt_val ) / (2 * a)])

lines = example.splitlines()

time = [int(x) for x in lines[0].split(":")[1].strip().split(" ") if x][0]
record = [int(x) for x in lines[1].split(":")[1].strip().split(" ") if x][0]

a, b = find_roots(1, time, record)
print(abs(math.floor(a) - math.floor(b)))
