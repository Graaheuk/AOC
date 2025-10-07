import time
import os
import sys
from collections import deque

# Reading input
start = time.time()

file_path = os.path.dirname(sys.argv[0])
f = open(file_path + '/input.dat','r')
lines = f.read().rstrip().split('\n')
end = time.time()
print("Time to read the file : " + str(end - start))
solutionStart = time.time()
# Solution 1

class Flipflop:
    pulseReturn = -1

    def __init__(self, name, output) -> None:
        self.name = name
        self.output = output

    def inPulse(self, pulse):
        if pulse == -1:
            self.pulseReturn = -self.pulseReturn

    def outPulse(self):
        return self.pulseReturn

class Conjunction:
    pulseReturn = -1

    def __init__(self, name, output) -> None:
        self.name = name
        self.output = output

    def inPulse(self, pulse):
        if pulse == -1:
            self.pulseReturn = -self.pulseReturn

    def outPulse(self):
        return self.pulseReturn

modules = dict()
for line in lines:
    splited = line.split(' -> ')
    modules[splited[0]] = splited[1].split(', ')

print(modules)
state = [('broadcaster', -1)]
queue = deque(state)
while queue:
    actual, pulse = queue.popleft()
    key=''
    for key in modules.keys():
        if actual in key:
            break
    if key == 'broadcaster':
        for i in modules[key]:
            queue.append((i, pulse))
    elif key[0] == '%':
        for i in modules[next]:
            queue.append((i, -pulse))
    elif key[0] == '&':
        for i in modules[next]:
            queue.append((i, -pulse))
    print()
    print(queue)

print("Part 1 : ", )
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()
# Solution 2


print("Part 2 : ", )
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))