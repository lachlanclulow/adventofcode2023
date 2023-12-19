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

work_flow_list = []
work_flow_map = {}
parts = []

parts_start = False
for line in example.splitlines():
    if parts_start:
        parts.append(
            dict(
                [(x.split("=")[0], int(x.split("=")[1])) for x in line.strip("{}").split(',')]
            )
        )
    if line == "":
        parts_start = True
    if not parts_start:
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
                    func = lambda x,y: x<y
                elif ">" in condition:
                    key, comparitor = condition.split(">")
                    comparitor = int(comparitor)
                    func = lambda x,y: x>y
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

def follow_work_flow(part, work_flow_key="in"):
    if work_flow_key in result:
        return result[work_flow_key]
    
    work_flow = work_flow_map[work_flow_key]

    for key, func, comparitor, action in work_flow:
        if key is None:
            if action in result:
                return result[action]
            return follow_work_flow(part, action)
        
        if func(part[key], comparitor):
            return follow_work_flow(part, action)



total = 0

for part in parts:
    if follow_work_flow(part):
        total += sum(part.values())

print(total)