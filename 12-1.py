example = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def parse_q(line, start_index, target_groupings, curr_groupings, grouping_index):
    if target_groupings[:grouping_index] != curr_groupings[:grouping_index]:
        return 0
    for i in range(start_index, len(line)):
        if line[i] == '?':
            return parse_q(line[:i]+"."+line[i+1:], i, target_groupings, curr_groupings.copy(), grouping_index) + \
                parse_q(line[:i]+"#"+line[i+1:], i, target_groupings, curr_groupings.copy(), grouping_index)
        elif line[i] == "#":
            curr_groupings[-1] += 1
            
        elif curr_groupings[-1] > 0:
            grouping_index += 1
            curr_groupings.append(0)

    while curr_groupings != [0] and curr_groupings[-1] == 0 and target_groupings[-1] != 0:
        curr_groupings = curr_groupings[:-1]

    if target_groupings == curr_groupings:
        return 1
    else:
        return 0

import re

rgx = re.compile("\.+")

total = 0
for line in example.splitlines():
    springs, groupings = line.split()
    springs = re.sub(rgx, ".", springs)
    total += parse_q(
        springs,
        0,
        [int(x) for x in groupings.split(',')],
        [0],
        0
    )

print(total)
