example = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

histories = []

for line in example.splitlines():
    n = [int(x) for x in line.split()]
    n.reverse() # remove for part 1 soln
    histories.append(n)

total = 0

def extrapolate(history):
    s = set(history[-1])
    if 0 in s and len(s) == 1:
        return 0
    
    diffs = []

    for i in range(1, len(history[-1])):
        diffs.append(history[-1][i] - history[-1][i-1])
    
    history.append(diffs)
    return history[-1][-1] + extrapolate(history)

for history in histories:
    total += history[-1] + extrapolate([history])

print(total)

