import time
import os
import sys

# Reading input
start = time.time()

file_path = os.path.dirname(sys.argv[0])
f = open(file_path + '/input.dat','r')
lines = f.read().rstrip().split('\n')
end = time.time()
print("Time to read the file : " + str(end - start))
solutionStart = time.time()
# Solution 1

def tiltWest(plateform):
    plat = plateform[::]
    for i in range(len(plateform)):
        tmp, tmp2 = '', ''
        found = False
        for j in range(len(plateform[i])):
            if plateform[i][j] != '#':
                tmp += plateform[i][j]
            else:
                found = True
                tmp = ''.join(sorted(tmp)[::-1]) + '#'
                tmp2 += tmp
                tmp = ''
        if found:
            plat[i] = tmp2 + ''.join(sorted(tmp)[::-1]) 
        else:
            plat[i] = ''.join(sorted(tmp)[::-1])
    return plat

def tiltNorth(lines):
    tmp = list(map(list, zip(*lines)))
    plateform = []
    for i in range(len(tmp)):
        plateform.append(''.join(tmp[i]))

    tiltPlateform = tiltWest(plateform)

    tmp = list(map(list, zip(*tiltPlateform)))
    tiltedPlateform = []
    for i in range(len(tmp)):
        tiltedPlateform.append(''.join(tmp[i]))
    return tiltedPlateform
    
tiltedPlateform = tiltNorth(lines)
res = 0
for i in range(len(tiltedPlateform)):
    for j in range(len(tiltedPlateform[i])):
        if tiltedPlateform[i][j] == 'O':
            res += len(tiltedPlateform) - i

print("Part 1 : ", res)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()
# Solution 2

def tiltSouth(lines):
    tmp = []
    for i in range(len(lines)):
        tmp.append(lines[i][::-1])

    tiltPlateform = tiltNorth(tmp)
    
    tiltedPlateform = []
    for i in range(len(tiltPlateform)):
        tiltedPlateform.append(tiltPlateform[i][::-1])
    return tiltedPlateform

def tiltEast(lines):
    tmp = []
    for i in range(len(lines)):
        tmp.append(lines[i][::-1])

    tiltPlateform = tiltWest(tmp)

    tiltedPlateform = []
    for i in range(len(tiltPlateform)):
        tiltedPlateform.append(tiltPlateform[i][::-1])
    return tiltedPlateform

def cycle(lines):
    t = tiltNorth(lines)
    t = tiltWest(t)
    t = tiltSouth(t)
    return tiltEast(t)

cycles = []
breake=False
for i in range(1000000000):
    if breake:
        break
    cy = cycle(lines)
    for cyCmp in cycles:
        if cy == cyCmp:
            print(i)
            breake=True
    else:
        lines = cy
        cycles.append(cy)

tiltedPlateform = cycles[1][::]
res = 0
for i in range(len(tiltedPlateform)):
    for j in range(len(tiltedPlateform[i])):
        if tiltedPlateform[i][j] == 'O':
            res += len(tiltedPlateform) - i

print("Part 2 : ", res)
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))