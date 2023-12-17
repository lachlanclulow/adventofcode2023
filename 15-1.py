example = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

def hash(s, start_val=0):
    start_val += ord(s[0])
    start_val *= 17
    start_val %= 256
    if len(s) == 1:
        return start_val
    return hash(s[1:], start_val)



total = 0
for command in example.split(','):
    total += hash(command)


print(total)