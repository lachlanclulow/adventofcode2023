example = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

def hash(s, start_val=0):
    start_val += ord(s[0])
    start_val *= 17
    start_val %= 256
    if len(s) == 1:
        return start_val
    return hash(s[1:], start_val)

loc = 0

boxes = {x: [] for x in range(256)}

def find_label(hash, label):
    for i, l in enumerate(boxes[hash]):
        if l[0] == label:
            return i
    return None

for command in example.split(','):
    if command[-1] == "-":
        # go to box and remove lens
        label = command.split('-')[0]
        h = hash(label)
        i = find_label(h, label)
        if i != None:
            boxes[h]=boxes[h][:i]+boxes[h][i+1:]
    else:
        label,flength = command.split('=')
        h = hash(label)
        i = find_label(h, label)
        if i == None:
            boxes[h].append((label, int(flength)))
        else:
            boxes[h]= boxes[h][:i] + [(label, int(flength))] + boxes[h][i+1:]
    

focusing_power = 0
for k, v in boxes.items():
    for i, lens in enumerate(v, 1):
        focusing_power += (1+k)*i*lens[1]

print(focusing_power)