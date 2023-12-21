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
    def __str__(self):
        return f"{self.id=} {self.memory=}"

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


src_module = None
# set up conjunctions
for module_id, module in modules.items():
    for target in module.targets:
        if target in conjunctions:
            modules[target].send_pulse(module_id, LOW)
        if target == "rx":
            src_module = module


loop_ends = [x for x in src_module.memory.keys()]


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
            if target in modules:
                modules[target].send_pulse(module.id, pulse)
                queue.append(modules[target])

i=0

resonance = [1] * len(loop_ends)


while not all([x>1 for x in resonance]):
    i+=1
    queue.append(Button("button", None))

    while queue:
        m = queue.pop(0)
        process_pulses(m)
        
        for j, loop_end in enumerate(loop_ends):
            if not all(modules[loop_end].memory.values()):
                resonance[j] = i

import math
print(math.lcm(*resonance))
