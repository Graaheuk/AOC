import time
import os
import sys
from functools import reduce
from math import lcm

# Reading input
start = time.time()

file_path = os.path.dirname(sys.argv[0])
f = open(file_path + '/input.dat','r')
lines = f.readlines()
end = time.time()
print("Time to read the file : " + str(end - start))
solutionStart = time.time()
# Solution 1

steps = lines[0].strip()

way = dict()
for path in lines[2:]:
    tmp = path.split(' = ')
    tmp2 = tmp[1].split(', ')
    way[tmp[0]] = (tmp2[0][1:], tmp2[1][:3])

step = 'AAA'
i, stepCount = 0, 0
while step != 'ZZZ':
    if steps[i % len(steps)] == 'L':
        step = way[step][0]
    else:
        step = way[step][1]
    stepCount += 1
    i += 1

print("Part 1 : ", stepCount)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()
# Solution 2

def arrived(position):
    for p in position:
        if p[-1]!='Z':
            return False
    return True

position = []
for step in way.keys():
    if step[-1] == 'A':
        position.append(step)

stepsCount = []
newStep = []
for step in position:
    i, stepCount = 0, 0
    while step[-1] != 'Z':
        if steps[i % len(steps)] == 'L':
            step = way[step][0]
        else:
            step = way[step][1]
        stepCount += 1
        i += 1
    stepsCount += [stepCount]
    newStep += [step]

res = reduce(lambda x,y:lcm(x,y), stepsCount)

print("Part 2 : ", res)
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))