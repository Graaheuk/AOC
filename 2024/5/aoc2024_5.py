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
res, res2 = 0, 0
dic = dict()

for line in lines:
    if '|' in line:
        a, b = line.split('|')
        if int(a) in dic.keys():
            dic[int(a)] += [int(b)]
        else: 
            dic[int(a)] = [int(b)]


def getOrder(dic):
    tmporder = []
    for i in dic.values():
        print(i)
    return tmporder

def checkOrder(line, dic):
    if len(line) <= 1:
        return True
    for j in line[1:]:
        if line[0] in dic.keys() and j in dic[line[0]]:
            return checkOrder(line[1:], dic)
        else:
            return False

def fix(tmp, order):
    ordre_index = {valeur: index for index, valeur in enumerate(order)}
    res = sorted(tmp, key=lambda x: ordre_index.get(x, float('inf')))
    return res


order = getOrder(dic)

for line in lines:
    if ',' in line:
        tmp = [int(num) for num in line.split(',')]
        if checkOrder(tmp, dic):
            res += int(tmp[len(tmp)//2])

# Solution 2
        else:
            tmp = fix(tmp, order)
            #print(int(tmp[len(tmp)//2]))
            res2 += int(tmp[len(tmp)//2])

print("Part 1 : ", res)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))

solution2Start = time.time()


print("Part 2 : ", res2)
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))
