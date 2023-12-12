import time
import os
import sys
import itertools

# Reading input
start = time.time()

file_path = os.path.dirname(sys.argv[0])
f = open(file_path + '/input.dat','r')
lines = [x.strip() for x in f.readlines()]
end = time.time()
print("Time to read the file : " + str(end - start))
solutionStart = time.time()
# Solution 1

def expandSpace(initialGalaxy):
    galaxy = []
    for line in initialGalaxy:
        if all(x=='.' for x in line):
            galaxy.append(line)
            galaxy.append(line)
        else: 
            galaxy.append(line)

    tmp = list(map(list, zip(*galaxy)))

    halfExpanded=[]
    for i in range(len(tmp)):
        halfExpanded.append(''.join(tmp[i]))

    galaxy = []
    for line in halfExpanded:
        if all(x=='.' for x in line):
            galaxy.append(line)
            galaxy.append(line)
        else: 
            galaxy.append(line)

    tmp = list(map(list, zip(*galaxy)))
    expandedGalaxy = []
    for i in range(len(tmp)):
        expandedGalaxy.append(''.join(tmp[i]))
    return expandedGalaxy

space = expandSpace(lines)

galaxies = []
for i in range(len(space)):
    for j in range(len(space[i])):
        if space[i][j]=='#':
            galaxies += [(i,j)]



pairs = []
while len(galaxies)>1:
    for i in range(1, len(galaxies)):
        pairs += [(galaxies[0],galaxies[i])]
    galaxies.pop(0)
    

res = 0
for left,right in pairs:
    res += abs(left[0]-right[0]) + abs(left[1] - right[1]) 

print("Part 1 : ", res)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()
# Solution 2

space = lines
emptyX, emptyY = [], []
emptyLine = ''.join(['.' for x in range(len(space[0]))])
emptyX = [i for i, x in enumerate(space) if x == emptyLine]

tmp = list(map(list, zip(*space)))
space = []
for i in range(len(tmp)):
    space.append(''.join(tmp[i]))

emptyLine = ''.join(['.' for x in range(len(space[0]))])
emptyY = [i for i, x in enumerate(space) if x == emptyLine]

tmp = list(map(list, zip(*space)))
space = []
for i in range(len(tmp)):
    space.append(''.join(tmp[i]))

galaxies = []
for i in range(len(space)):
    for j in range(len(space[i])):
        if space[i][j]=='#':
            galaxies += [(i,j)]

pairs = []
while len(galaxies)>1:
    for i in range(1, len(galaxies)):
        pairs += [(galaxies[0],galaxies[i])]
    galaxies.pop(0)

res = 0
for pair in pairs:
    toAdd = 0
    for x in emptyX:
        if pair[0][0] < x and pair[1][0] > x or pair[0][0] > x and pair[1][0] < x:
            toAdd += 1000000
    for y in emptyY:
        if pair[0][1] < y and pair[1][1] > y or pair[0][1] > y and pair[1][1] < y:
            toAdd += 1000000
    res += abs(pair[0][0]-pair[1][0]) + abs(pair[0][1] - pair[1][1]) + toAdd

print("Part 2 : ", res-82)
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))