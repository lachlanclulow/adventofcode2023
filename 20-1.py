example = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

example = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

ON = True
OFF = False

HIGH = True
LOW = False

modules = {}
flip_flops = {}
conjunctions = set()

flip_flop_state = {}

queue = []

class FlipFlop:
    def __init__(self, id, targets):
        self.id = id
        self.state = OFF
        self.flipped = False
        self.targets = targets
    def send_pulse(self, src: str, pulse: bool):
        if pulse == LOW:
            self.state = not self.state
            self.flipped = True
    def process(self):
        if self.flipped:
            self.flipped = False
            if self.state == OFF:
                return LOW
            else:
                return HIGH
        return None
    
class Conjunction:
    def __init__(self, id, targets):
        self.id = id
        self.memory = {}
        self.targets = targets
    def send_pulse(self, src: str, pulse: bool):
        self.memory[src] = pulse
    def process(self):
        pulse = not all(self.memory.values())
        return pulse

class Broadcaster:
    def __init__(self, id, targets):
        self.id = id
        self.targets = targets
        self.pulse = None
    def send_pulse(self, src: str, pulse: bool):
        self.pulse = pulse
    def process(self):
        return self.pulse

class Button:
    def __init__(self, id, targets):
        self.id = id
        self.targets = ["broadcaster"]
    def send_pulse(self, src: str, pulse: bool):
        pass
    def process(self):
        return LOW

for line in example.splitlines():
    src, target = line.split(" -> ")
    targets = [x.strip() for  x in target.split(',')]
    if src[0] == "%":
        modules[src[1:]] = FlipFlop(src[1:], targets)
    elif src[0] == "&":
        modules[src[1:]] = Conjunction(src[1:], targets)
        conjunctions.add(src[1:])
    else:
        modules[src] = Broadcaster(src, targets)

# set up conjunctions
for module_id, module in modules.items():
    for target in module.targets:
        if target in conjunctions:
            modules[target].send_pulse(module_id, LOW)

queue = []

pulses = {
    HIGH: 0,
    LOW: 0
}

rx = HIGH

def process_pulses(module):
    pulse = module.process()
    if pulse is not None:
        for target in module.targets:
            #print(f"{module.id} -{'high' if pulse else 'low'}-> {target}")
            pulses[pulse]+=1
            if target in modules:
                modules[target].send_pulse(module.id, pulse)
                queue.append(modules[target])


for i in range(1000):
    queue.append(Button("button", None))

    while queue:
        m = queue.pop(0)
        process_pulses(m)


print(pulses)
print(pulses[HIGH] * pulses[LOW])
