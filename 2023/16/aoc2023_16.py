import time
import os
import sys

# Reading input
start = time.time()

# FIND AND REPLACE '\' WITH 'A' ON THE INPUT FILE

file_path = os.path.dirname(sys.argv[0])
f = open(file_path + "/input.dat",'r')
mirror = f.read().rstrip().split('\n')
end = time.time()
print("Time to read the file : " + str(end - start))
solutionStart = time.time()
# Solution 1

sys.setrecursionlimit(10000)

LEFT, RIGHT, UP, DOWN = (0,-1), (0,1), (-1,0), (1,0)

def printT(lines):
    for i in lines:
        print(i)
    print()

def showMap(mirror, seen):
    res = set()
    for line in seen:
        res.add((line[0], line[1]))
    for i in range(len(mirror)):
        tmp = ''
        for j in range(len(mirror[i])):
            if (i,j) in res:
                tmp += '#'
            else:
                tmp += mirror[i][j]
        print(tmp)
    print()

def countRes(seen):
    res = set()
    for line in seen:
        res.add((line[0], line[1]))
    return len(res)

def goRight(mirror, pos, seen):
    nextPos = (pos[0] + RIGHT[0], pos[1] + RIGHT[1])
    if [pos[0], pos[1], 'r'] in seen:
        return
    seen += [[pos[0], pos[1], 'r']]
    if nextPos[1] >= len(mirror[0]):
        return
    if mirror[nextPos[0]][nextPos[1]] in '.-':
        goRight(mirror, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '|':
        goUp(mirror, nextPos, seen)
        goDown(mirror, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '/':
        goUp(mirror,  nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == 'A':
        goDown(mirror, nextPos, seen)

def goLeft(mirror, pos, seen):
    nextPos = (pos[0] + LEFT[0], pos[1] + LEFT[1])
    if [pos[0], pos[1], 'l'] in seen:
        return
    seen += [[pos[0], pos[1], 'l']]
    if nextPos[1] < 0:
        return
    if mirror[nextPos[0]][nextPos[1]] in '.-':
        goLeft(mirror, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '|':
        goUp(mirror, nextPos, seen)
        goDown(mirror, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '/':
        goDown(mirror, nextPos, seen) 
    elif mirror[nextPos[0]][nextPos[1]] == 'A':
        goUp(mirror, nextPos, seen)

def goUp(mirror, pos, seen):
    nextPos = (pos[0] + UP[0], pos[1] + UP[1])
    if [pos[0], pos[1], 'u'] in seen:
        return
    seen += [[pos[0], pos[1], 'u']]
    if nextPos[0] < 0:
        return
    if mirror[nextPos[0]][nextPos[1]] in '.|':
        goUp(mirror, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '-':
        goLeft(mirror, nextPos, seen)
        goRight(mirror, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '/':
        goRight(mirror, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == 'A':
        goLeft(mirror, nextPos, seen)

def goDown(mirror, pos, seen):
    nextPos = (pos[0] + DOWN[0], pos[1] + DOWN[1])
    if [pos[0], pos[1], 'd'] in seen:
        return
    seen += [[pos[0], pos[1], 'd']]
    if nextPos[0] >= len(mirror):
        return
    if mirror[nextPos[0]][nextPos[1]] in '.|':
        goDown(mirror, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '-':
        goLeft(mirror, nextPos, seen)
        goRight(mirror, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '/':
        goLeft(mirror, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == 'A':
        goRight(mirror, nextPos, seen)

pos = (0,0)
seen = []

if mirror[0][0] == '.':
    goRight(mirror, pos, seen)
else:
    goDown(mirror, pos, seen)

print("Part 1 : ", countRes(seen))
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()
# Solution 2

def startFromLeft(mirror, pos):
    seen = []
    if mirror[pos[0]][pos[1]] in '.-':
        goRight(mirror, pos, seen)
    if mirror[pos[0]][pos[1]] == '/':
        goUp(mirror, pos, seen)
    if mirror[pos[0]][pos[1]] == 'A':
        goDown(mirror, pos, seen)
    if mirror[pos[0]][pos[1]] == '|':
        goUp(mirror, pos, seen)
        goDown(mirror, pos, seen)
    return countRes(seen)

def startFromRight(mirror, pos):
    seen = []
    if mirror[pos[0]][pos[1]] in '.-':
        goLeft(mirror, pos, seen)
    if mirror[pos[0]][pos[1]] == '/':
        goDown(mirror, pos, seen)
    if mirror[pos[0]][pos[1]] == 'A':
        goUp(mirror, pos, seen)
    if mirror[pos[0]][pos[1]] == '|':
        goDown(mirror, pos, seen)
        goUp(mirror, pos, seen)
    return countRes(seen)

def startFromDown(mirror, pos):
    seen = []
    if mirror[pos[0]][pos[1]] in '.|':
        goUp(mirror, pos, seen)
    if mirror[pos[0]][pos[1]] == '/':
        goRight(mirror, pos, seen)
    if mirror[pos[0]][pos[1]] == 'A':
        goLeft(mirror, pos, seen)
    if mirror[pos[0]][pos[1]] == '-':
        goLeft(mirror, pos, seen)
        goRight(mirror, pos, seen)
    return countRes(seen)

def startFromUp(mirror, pos):
    seen = []
    if mirror[pos[0]][pos[1]] in '.|':
        goDown(mirror, pos, seen)
    if mirror[pos[0]][pos[1]] == '/':
        goLeft(mirror, pos, seen)
    if mirror[pos[0]][pos[1]] == 'A':
        goRight(mirror, pos, seen)
    if mirror[pos[0]][pos[1]] == '-':
        goLeft(mirror, pos, seen)
        goRight(mirror, pos, seen)
    return countRes(seen)

best = []
for i in range(0,len(mirror)):
    best.append(startFromLeft(mirror, (i, 0)))
    best.append(startFromDown(mirror, (len(mirror[0])-1, i)))
    best.append(startFromRight(mirror, (i, len(mirror)-1)))
    best.append(startFromUp(mirror, (0, i)))

print("Part 2 : ", max(best))
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))