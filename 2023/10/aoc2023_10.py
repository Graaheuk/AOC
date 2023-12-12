import time
import os
import sys

# Reading input
start = time.time()

file_path = os.path.dirname(sys.argv[0])
f = open(file_path + '/input.dat','r')
lines = f.readlines()
end = time.time()
print("Time to read the file : " + str(end - start))
solutionStart = time.time()
# Solution 1

WAYS = ['|','-','F','J','L','7']

def findWaysFromStart(lines, startPos):
    res = []
    if lines[startPos[0] - 1][startPos[1]] in '|F7':
        res += [(startPos[0] - 1, startPos[1])]
    if lines[startPos[0] + 1][startPos[1]] in '|JL':
        res += [(startPos[0] + 1, startPos[1])]
    if lines[startPos[0]][startPos[1] - 1] in '-FL':
        res += [(startPos[0], startPos[1] - 1)]
    if lines[startPos[0]][startPos[1] + 1] in '-J7':
        res += [(startPos[0], startPos[1] + 1)]
    return res

def nextStep(lines, lastLeft, left, lastRight, right):
    newLeft, newRight= (0,0), (0,0)

    #LEFT
    if lines[left[0]][left[1]] == '|':
        if lastLeft[0] > left[0]:
            newLeft = (left[0] - 1, left[1])
        else:
            newLeft = (left[0] + 1, left[1])
    elif lines[left[0]][left[1]] == '-':
        if lastLeft[1] > left[1]:
            newLeft = (left[0], left[1] - 1)
        else:
            newLeft = (left[0], left[1] + 1)
    elif lines[left[0]][left[1]] == '7':
        if lastLeft[1] < left[1]:
            newLeft = (left[0] + 1, left[1])
        else:
            newLeft = (left[0], left[1] - 1 )
    elif lines[left[0]][left[1]] == 'L':
        if lastLeft[0] < left[0]:
            newLeft = (left[0] - 1, left[1])
        else:
            newLeft = (left[0], left[1] + 1)
    elif lines[left[0]][left[1]] == 'J':
        if lastLeft[1] < left[1]:
            newLeft = (left[0] - 1, left[1])
        else:
            newLeft = (left[0], left[1] - 1)
    elif lines[left[0]][left[1]] == 'F':
        if lastLeft[1] > left[1]:
            newLeft = (left[0] + 1, left[1])
        else:
            newLeft = (left[0], left[1] + 1)

    # RIGHT
    if lines[right[0]][right[1]] == '|':
        if lastRight[0] > right[0]:
            newRight = (right[0] - 1, right[1])
        else:
            newRight = (right[0] + 1, right[1])
    elif lines[right[0]][right[1]] == '-':
        if lastRight[1] > right[1]:
            newRight = (right[0], right[1] - 1)
        else:
            newRight = (right[0], right[1] + 1)
    elif lines[right[0]][right[1]] == '7':
        if lastRight[1] < right[1]:
            newRight = (right[0] + 1, right[1])
        else:
            newRight = (right[0], right[1] - 1)
    elif lines[right[0]][right[1]] == 'L':
        if lastRight[0] < right[0]:
            newRight = (right[0] - 1, right[1])
        else:
            newRight = (right[0], right[1] + 1)
    elif lines[right[0]][right[1]] == 'J':
        if lastRight[1] < right[1]:
            newRight = (right[0] - 1, right[1])
        else:
            newRight = (right[0], right[1] - 1)
    elif lines[right[0]][right[1]] == 'F':
        if lastRight[1] > right[1]:
            newRight = (right[0] + 1, right[1])
        else:
            newRight = (right[0], right[1] + 1)
    return newLeft, newRight

l = []
startPos = ()
for i in range(len(lines)):
    l += [x for x in lines[i].strip().split()]
    if 'S' in lines[i]:
        startPos = (i, lines[i].index('S'))


stepCount = 0
oldLeft, oldRight = startPos, startPos
left, right = findWaysFromStart(l, startPos)
while left != right:
    print(left, right)
    tmpLeft, tmpRight = left, right
    left, right = nextStep(lines, oldLeft, left, oldRight, right)
    oldLeft, oldRight = tmpLeft, tmpRight
    stepCount += 1

print(startPos)
print("Part 1 : ", stepCount)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()
# Solution 2



print("Part 2 : ", )
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))