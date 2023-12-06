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

# Solution
solutionStart = time.time()

def findTotalNumber(lines, x, y):
    if lines[x][y].isdigit():
        totalNumber = str(lines[x][y])
        startY = y
        y -= 1
        char = lines[x][y]
        while char.isdigit() and y > -1:
            totalNumber = char + totalNumber
            y -= 1
            char = lines[x][y]
        y = startY + 1
        char = lines[x][y]
        while char.isdigit() and y < len(lines[x]) + 1:
            totalNumber = totalNumber + char
            y += 1
            char = lines[x][y]
        return totalNumber
    else:
        return 0

totalSum = 0
for x in range(1,len(lines)-1):
    stripped = lines[x].strip()
    for y in range(1,len(stripped)-1):
        totalSet = set()
        if not lines[x][y].isdigit() and lines[x][y] != '.':
            for i in range(-1,2):
                for j in range(-1,2):
                    totalSet.add(int(findTotalNumber(lines, x+i, y+j)))
        for toAdd in totalSet: 
            totalSum += toAdd

print("Part 1 : ", totalSum)

print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()

totalSum = 0
for x in range(1,len(lines)-1):
    stripped = lines[x].strip()
    for y in range(1,len(stripped)-1):
        totalSet = set()
        if lines[x][y]=='*':
            for i in range(-1,2):
                for j in range(-1,2):
                    totalSet.add(int(findTotalNumber(lines, x+i, y+j)))
        totalSet.discard(0)
        if len(totalSet)==2:
            gearRatio = 1
            for toMult in totalSet: 
                gearRatio *= toMult
            totalSum += gearRatio

print("Part 2 : ", totalSum)

end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))