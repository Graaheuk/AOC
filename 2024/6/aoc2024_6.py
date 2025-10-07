from operator import concat, contains
import time
import os
import sys
import re

from numpy import character

# Reading input
start = time.time()

file_path = os.path.dirname(sys.argv[0])
f = open(file_path + '/input.dat','r')
lines = f.readlines()
end = time.time()
print("Time to read the file : " + str(end - start))
solutionStart = time.time()
# Solution 1
res = 0
store = []

def getUp(pos):
    return (pos[0]-1, pos[1])

def getDown(pos):
    return (pos[0]+1, pos[1])

def getRight(pos):
    return (pos[0], pos[1]+1)

def getLeft(pos):
    return (pos[0], pos[1]-1)


def move(pos, store):
    orientation = '^'
    seen = set(pos)
    while pos[0] >= 0 and pos[0] < len(store) and pos[1] >= 0 and pos[1] < len(store[0]):
        if orientation == '^':
            nextPos = getUp(pos)
            if nextPos[0] == -1 or nextPos[0] == len(store) or nextPos[1] == -1 or nextPos[1] == len(store[0]):
                return len(seen)
            if store[nextPos[0]][nextPos[1]] == '#':
                orientation = '>'
            else:
                seen.add(pos)
                pos = nextPos
        elif orientation == 'v':
            nextPos = getDown(pos)
            if nextPos[0] == -1 or nextPos[0] == len(store) or nextPos[1] == -1 or nextPos[1] == len(store[0]):
                return len(seen)
            if store[nextPos[0]][nextPos[1]] == '#':
                orientation = '<'
            else:
                seen.add(pos)
                pos = nextPos
        elif orientation == '<':
            nextPos = getLeft(pos)
            if nextPos[0] == -1 or nextPos[0] == len(store) or nextPos[1] == -1 or nextPos[1] == len(store[0]):
                return len(seen)
            if store[nextPos[0]][nextPos[1]] == '#':
                orientation = '^'
            else:
                seen.add(pos)
                pos = nextPos
        elif orientation == '>':
            nextPos = getRight(pos)
            if nextPos[0] == -1 or nextPos[0] == len(store) or nextPos[1] == -1 or nextPos[1] == len(store[0]):
                return len(seen)
            if store[nextPos[0]][nextPos[1]] == '#':
                orientation = 'v'
            else:
                seen.add(pos)
                pos = nextPos

pos = (0,0)
for i in range(len(lines)):
    if '^' in lines[i]:
        pos = i, lines[i].index('^')
    store += lines[i].strip().split(",")

res = move(pos, store) - 1 

print(store)
print("Part 1 : ", res)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))

solution2Start = time.time()


print("Part 2 : ", res)
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))
