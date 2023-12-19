example = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

from functools import reduce

work_flow_list = []
work_flow_map = {}

for line in example.splitlines():
    if line == "":
        break

    work_flow_name, actions = line.split("{")
    work_flow_list.append(work_flow_name)

    work_flow_map[work_flow_name] = []
    for rule in actions.strip("}").split(','):
        condition, action, key, comparitor, func = (None, None, None, None, None)
        try:
            condition, action = rule.split(":")
            if "<" in condition:
                key, comparitor = condition.split("<")
                comparitor = int(comparitor)
                func = "<"
            elif ">" in condition:
                key, comparitor = condition.split(">")
                comparitor = int(comparitor)
                func = ">"
        except ValueError as e:
            action = rule
        work_flow_map[work_flow_name].append(
            (
                key,
                func,
                comparitor,
                action
            )
        )

            
result = {
    "R": False,
    "A": True
}

def follow_work_flow(x=(1, 4000), m=(1, 4000), a=(1, 4000), s=(1, 4000), work_flow_key="in"):
    if work_flow_key in result:
        if result[work_flow_key]:
            return set(((x, m, a, s),))
        else:
            return set()
    
    work_flow = work_flow_map[work_flow_key]

    acceptable_ranges = set()

    for key, func, comparitor, action in work_flow:
        if key is None:
            if action in result:
                if result[action]:
                    return acceptable_ranges.union(set(((x, m, a, s),)))
            acceptable_ranges = acceptable_ranges.union(
                set(follow_work_flow(x, m, a, s, action))
            )
        

        n_x, n_m, n_a, n_s = x, m, a, s
        
        match key, func:
            case 'x', '<':
                n_x = (x[0], comparitor-1)
                x = (comparitor, x[1])
            case 'x', '>':
                n_x = (comparitor+1, x[1])
                x = (x[0], comparitor)
            case 'm', '<':
                n_m = (m[0], comparitor-1)
                m = (comparitor, m[1])
            case 'm', '>':
                n_m = (comparitor+1, m[1])
                m = (m[0], comparitor)
            case 'a', '<':
                n_a = (a[0], comparitor-1)
                a = (comparitor, a[1])
            case 'a', '>':
                n_a = (comparitor+1, a[1])
                a = (a[0], comparitor)
            case 's', '<':
                n_s = (s[0], comparitor-1)
                s = (comparitor, s[1])
            case 's', '>':
                n_s = (comparitor+1, s[1])
                s = (s[0], comparitor)

        acceptable_ranges = acceptable_ranges.union(
            set(follow_work_flow(n_x, n_m, n_a, n_s, action))
        )
    return acceptable_ranges


total = sum(
    [
        reduce(
            (lambda x,y: x*y),
            [b-a+1 for a,b in x]
        ) for x in follow_work_flow()
    ]
)

print(total)