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

def getLastElement(l):
    tmp = []
    for i in range(len(l) - 1):
        tmp.append(l[i+1] - l[i])
    if all(x == 0 for x in tmp):
        return l[-1]
    else:
        return l[-1] + getLastElement(tmp)

res = 0
for line in lines:
    l = [int(x) for x in line.strip().split()]
    res += getLastElement(l)

print("Part 1 : ", res)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()
# Solution 2

def getFirstElement(l):
    tmp = []
    for i in range(len(l) - 1):
        tmp.append(l[i+1] - l[i])
    if all(x == 0 for x in tmp):
        return l[0]
    else:
        return l[0] - getFirstElement(tmp)

res = 0
for line in lines:
    l = [int(x) for x in line.strip().split()]
    res += getFirstElement(l)

print("Part 2 : ", res)
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))