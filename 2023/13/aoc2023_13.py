import time
import os
import sys

# Reading input
start = time.time()

file_path = os.path.dirname(sys.argv[0])
f = open(file_path + '/input.dat','r')
lines = f.read().strip()
end = time.time()
print("Time to read the file : " + str(end - start))
solutionStart = time.time()
# Solution 1

patterns = lines.split('\n\n')
patternList = []
for pat in patterns:
    patternList.append(pat.split('\n'))

def findHMirror(pattern):
    for i in range(1,len(pattern)):
        tmp = pattern[0:i]
        tmp2 = pattern[i:i+len(pattern[0:i])][::-1]
        if len(tmp) > len(tmp2):
            tmp = tmp[len(tmp)-len(tmp2):]
        if tmp == tmp2:
            return i
    return 0

def findVMirror(pattern):
    tmp = list(map(list, zip(*pattern)))
    tmpPattern = []
    for i in range(len(tmp)):
        tmpPattern.append(''.join(tmp[i]))
    return findHMirror(tmpPattern)

res = 0
for pattern in patternList:
    h = findHMirror(pattern)
    v = findVMirror(pattern)
    res += v + 100 * h

print("Part 1 : ", res)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()
# Solution 2

def findHMirror2(pattern, old):
    for i in range(1,len(pattern)):
        tmp = pattern[0:i]
        tmp2 = pattern[i:i+len(pattern[0:i])][::-1]
        if len(tmp) > len(tmp2):
            tmp = tmp[len(tmp)-len(tmp2):]
        if tmp == tmp2 and i != old:
            return i
    return 0

def findVMirror2(pattern, old):
    tmp = list(map(list, zip(*pattern)))
    tmpPattern = []
    for i in range(len(tmp)):
        tmpPattern.append(''.join(tmp[i]))
    return findHMirror2(tmpPattern, old)

def findNewMirror(pattern, old):
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            tmp = pattern[::]
            if pattern[i][j]=="#":
                tmp[i] = pattern[i][:j] + "." + pattern[i][j+1:len(pattern[i])]
            else:
                tmp[i] = pattern[i][:j] + "#" + pattern[i][j+1:len(pattern[i])]
            h = 100 * findHMirror2(tmp, old)
            if h != 0:
                return h
            else:
                v = findVMirror2(tmp, old)
                if v != 0:
                    return v
    return 0

res = 0
for pattern in patternList:
    old = findHMirror(pattern) + findVMirror(pattern)
    res += findNewMirror(pattern, old)

print("Part 2 : ", res)
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))