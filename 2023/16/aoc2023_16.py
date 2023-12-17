import time
import os
import sys

# Reading input
start = time.time()

# FIND AND REPLACE '\' WITH 'A'

file_path = os.path.dirname(sys.argv[0])
f = open(file_path + "/input.dat",'r')
mirror = f.read().rstrip().split('\n')
end = time.time()
print("Time to read the file : " + str(end - start))
solutionStart = time.time()
# Solution 1

sys.setrecursionlimit(10000)

def printT(lines):
    for i in lines:
        print(i)
    print()

def initLight():
    light = []
    for line in mirror:
        tmp = ''
        for c in line:
            tmp += '.'
        light += [tmp]
    return light

LEFT, RIGHT, UP, DOWN = (0,-1), (0,1), (-1,0), (1,0)

def goRight(mirror, light, pos, seen):
    light[pos[0]] = light[pos[0]][:pos[1]] + '#' + light[pos[0]][pos[1]+1:]
    nextPos = (pos[0] + RIGHT[0], pos[1] + RIGHT[1])
    if (pos[0], pos[1], 'r') in seen or nextPos[1] >= len(mirror[0]):
        return
    seen += (pos[0], pos[1], 'r')
    if mirror[nextPos[0]][nextPos[1]] == '.':
        goRight(mirror, light, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '-':
        if light[nextPos[0]][nextPos[1]] == '#':
            return
        goRight(mirror, light, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '|':
        if light[nextPos[0]][nextPos[1]] == '#':
            return
        goUp(mirror, light, nextPos, seen)
        goDown(mirror, light, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '/':
        goUp(mirror, light, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == 'A':
        goDown(mirror, light, nextPos, seen)

def goLeft(mirror, light, pos, seen):
    light[pos[0]] = light[pos[0]][:pos[1]] + '#' + light[pos[0]][pos[1]+1:]
    nextPos = (pos[0] + LEFT[0], pos[1] + LEFT[1])
    if (pos[0], pos[1], 'l') in seen or nextPos[1] < 0:
        return
    seen += (pos[0], pos[1], 'l')
    if mirror[nextPos[0]][nextPos[1]] == '.':
        goLeft(mirror, light, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '-':
        if light[nextPos[0]][nextPos[1]] == '#':
            return
        goLeft(mirror, light, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '|':
        if light[nextPos[0]][nextPos[1]] == '#':
            return
        goUp(mirror, light, nextPos, seen)
        goDown(mirror, light, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '/':
        goDown(mirror, light, nextPos, seen) 
    elif mirror[nextPos[0]][nextPos[1]] == 'A':
        goUp(mirror, light, nextPos, seen)

def goUp(mirror, light, pos, seen):
    light[pos[0]] = light[pos[0]][:pos[1]] + '#' + light[pos[0]][pos[1]+1:]
    nextPos = (pos[0] + UP[0], pos[1] + UP[1])
    if (pos[0], pos[1], 'u') in seen or nextPos[0] < 0:
        return
    seen += (pos[0], pos[1], 'u')
    if mirror[nextPos[0]][nextPos[1]] == '.':
        goUp(mirror, light, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '-':
        if light[nextPos[0]][nextPos[1]] == '#':
            return
        goLeft(mirror, light, nextPos, seen)
        goRight(mirror, light, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '|':
        if light[nextPos[0]][nextPos[1]] == '#':
            return
        goUp(mirror, light, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '/':
        goRight(mirror, light, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == 'A':
        goLeft(mirror, light, nextPos, seen)

def goDown(mirror, light, pos, seen):
    light[pos[0]] = light[pos[0]][:pos[1]] + '#' + light[pos[0]][pos[1]+1:]
    nextPos = (pos[0] + DOWN[0], pos[1] + DOWN[1])
    if (pos[0], pos[1], 'd') in seen or nextPos[0] >= len(mirror):
        return
    seen += (pos[0], pos[1], 'd')
    if mirror[nextPos[0]][nextPos[1]] == '.':
        goDown(mirror, light, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '-':
        if light[nextPos[0]][nextPos[1]] == '#':
            return
        goLeft(mirror, light, nextPos, seen)
        goRight(mirror, light, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '|':
        if light[nextPos[0]][nextPos[1]] == '#':
            return
        goDown(mirror, light, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == '/':
        goLeft(mirror, light, nextPos, seen)
    elif mirror[nextPos[0]][nextPos[1]] == 'A':
        goRight(mirror, light, nextPos, seen)

pos = (0,0)
seen = []
light = initLight()

if mirror[0][0] == '.':
    goRight(mirror, light, pos, seen)
else:
    goDown(mirror, light, pos, seen)

res = 0
for line in light:
    res += line.count('#')

print("Part 1 : ", res)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()
# Solution 2

def startFromLeft(mirror, pos, seen):
    light = initLight()
    if mirror[pos[0]][pos[1]] in '.-':
        goRight(mirror, light, pos, seen)
    if mirror[pos[0]][pos[1]] in '/':
        goUp(mirror, light, pos, seen)
    if mirror[pos[0]][pos[1]] in 'A':
        goDown(mirror, light, pos, seen)
    if mirror[pos[0]][pos[1]] in '|':
        goUp(mirror, light, pos, seen)
        goDown(mirror, light, pos, seen)
    res = 0
    for line in light:
        res += line.count('#')
    return res

def startFromRight(mirror, pos, seen):
    light = initLight()
    if mirror[pos[0]][pos[1]] in '.-':
        goLeft(mirror, light, pos, seen)
    if mirror[pos[0]][pos[1]] in '/':
        goDown(mirror, light, pos, seen)
    if mirror[pos[0]][pos[1]] in 'A':
        goUp(mirror, light, pos, seen)
    if mirror[pos[0]][pos[1]] in '|':
        goDown(mirror, light, pos, seen)
        goUp(mirror, light, pos, seen)
    res = 0
    for line in light:
        res += line.count('#')
    return res

def startFromDown(mirror, pos, seen):
    light = initLight()
    if mirror[pos[0]][pos[1]] in '.|':
        goUp(mirror, light, pos, seen)
    if mirror[pos[0]][pos[1]] in '/':
        goRight(mirror, light, pos, seen)
    if mirror[pos[0]][pos[1]] in 'A':
        goLeft(mirror, light, pos, seen)
    if mirror[pos[0]][pos[1]] in '-':
        goLeft(mirror, light, pos, seen)
        goRight(mirror, light, pos, seen)
    res = 0
    for line in light:
        res += line.count('#')
    return res

def startFromUp(mirror, pos, seen):
    light = initLight()
    if mirror[pos[0]][pos[1]] in '.|':
        goDown(mirror, light, pos, seen)
    if mirror[pos[0]][pos[1]] in '/':
        goLeft(mirror, light, pos, seen)
    if mirror[pos[0]][pos[1]] in 'A':
        goRight(mirror, light, pos, seen)
    if mirror[pos[0]][pos[1]] in '-':
        goLeft(mirror, light, pos, seen)
        goRight(mirror, light, pos, seen)
    res = 0
    for line in light:
        res += line.count('#')
    return res

best = 0
for i in range(0,len(mirror),2):
    print(i)
    best = max(startFromUp(mirror, (i, 0), seen), best)
    best = max(startFromRight(mirror, (len(mirror[0])-1, i), seen), best)
    best = max(startFromDown(mirror, (i, len(mirror)-1), seen), best)
    best = max(startFromLeft(mirror, (0, i), seen), best)

print("Part 2 : ", best)
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))