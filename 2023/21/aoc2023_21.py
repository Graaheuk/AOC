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

LEFT, RIGHT, UP, DOWN = (0,-1), (0,1), (-1,0), (1,0)
DIRECTIONS = [LEFT, RIGHT, UP, DOWN]

sPos = (0,0)
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j]=='S':
            sPos = (i,j)

stepToDo = 6
stepCount = 0
queue = deque([[sPos]])
totalPosition = set()
totalPosition.add(sPos)
while queue and stepCount <= stepToDo:
    posi = queue.popleft()
    tmpPosition = set()
    for x, y in posi:
        for direction in DIRECTIONS:
            newPos = (x + direction[0], y + direction[1])
            if lines[newPos[0]][newPos[1]] != '#' and not newPos in totalPosition and 0 <= newPos[0] < len(lines) and 0 <= newPos[1] < len(lines[0]): 
                tmpPosition.add(newPos)
    stepCount += 1
    newTmpPos = set()
    for x, y in tmpPosition:
        for direction in DIRECTIONS:
            newPos = (x + direction[0], y + direction[1])
            if 0 <= newPos[0] < len(lines) and 0 <= newPos[1] < len(lines[0]) and lines[newPos[0]][newPos[1]] != '#' and not newPos in totalPosition: 
                newTmpPos.add(newPos)
                totalPosition.add(newPos)
    queue.append(list(newTmpPos))
    stepCount += 1


print(totalPosition)

print("Part 1 : ", len(totalPosition))
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()
# Solution 2


print("Part 2 : ", )
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))