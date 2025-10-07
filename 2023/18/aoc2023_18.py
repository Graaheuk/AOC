import time
import os
import sys
from itertools import pairwise

# Reading input
start = time.time()

file_path = os.path.dirname(sys.argv[0])
f = open(file_path + '/input.dat','r')
lines = f.read().rstrip().split('\n')
end = time.time()
print("Time to read the file : " + str(end - start))
solutionStart = time.time()
# Solution 1

LEFT, RIGHT, UP, DOWN = (0,-1), (0,1), (-1,0), (1,0)

def getDimension(terrain):
    minX, minY, maxX, maxY = 0, 0, 0, 0
    for i in terrain:
        if i[0] > maxX:
            maxX = i[0]
        elif i[0] < minX:
            minX = i[0]
        if i[1] > maxY:
            maxY = i[1]
        elif i[1] < minY:
            minY = i[1]
    return (maxX, minX, maxY, minY)

def shoelace(points):
    return abs(sum(
        (x1 * y2) - (y1 * x2)
        for (x1, y1), (x2, y2) in pairwise(tuple(points) + (points[0],))
    )) / 2
    
plan = []
for line in lines:
    plan += [line.split()]


terrain = []
actual = (0,0)
boundary = 0
for direction in plan:
    boundary += int(direction[1])
    if direction[0]=='R':
        for i in range(int(direction[1])):
            actual = (actual[0] + RIGHT[0], actual[1] + RIGHT[1])
            terrain.append(actual)
    if direction[0]=='L':
        for i in range(int(direction[1])):
            actual = (actual[0] + LEFT[0], actual[1] + LEFT[1])
            terrain.append(actual)
    if direction[0]=='D':
        for i in range(int(direction[1])):
            actual = (actual[0] + DOWN[0], actual[1] + DOWN[1])
            terrain.append(actual)
    if direction[0]=='U':
        for i in range(int(direction[1])):
            actual = (actual[0] + UP[0], actual[1] + UP[1])
            terrain.append(actual)

res = int(shoelace(terrain)) + boundary // 2 + 1


print("Part 1 : ", res)

end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()
# Solution 2

terrain = []
actual = (0,0)
boundary = 0
for line in lines:
    inp = line.split()[2]
    direction = int(inp[2:7],16)
    boundary += direction
    if inp[7]=='0':
        actual = (actual[0] + RIGHT[0] * direction, actual[1] + RIGHT[1] * direction)
        terrain.append(actual)
    if inp[7]=='1':
        actual = (actual[0] + DOWN[0] * direction, actual[1] + DOWN[1] * direction)
        terrain.append(actual)
    if inp[7]=='2':
        actual = (actual[0] + LEFT[0] * direction, actual[1] + LEFT[1] * direction)
        terrain.append(actual)
    if inp[7]=='3':
        actual = (actual[0] + UP[0] * direction, actual[1] + UP[1] * direction)
        terrain.append(actual)

res = int(shoelace(terrain)) + boundary // 2 + 1

print("Part 2 : ", res)
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))