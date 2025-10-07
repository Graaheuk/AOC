from operator import contains
import time
import os
import sys
import re

from numpy import character

# Reading input
start = time.time()

file_path = os.path.dirname(sys.argv[0])
f = open('C:/Users/Graaheuk/Desktop/AOC/2024/4/input.dat','r')
lines = f.readlines()
end = time.time()
print("Time to read the file : " + str(end - start))
solutionStart = time.time()
# Solution 1

length = 3

def checkXmax(lines, i, j):
    tmp_res = 0
    if i >= length and lines[i-1][j]=='M' and lines[i-2][j]=='A' and lines[i-3][j]=='S': 
        tmp_res += 1 # GAUCHE
    if i < len(lines) - length and lines[i+1][j]=='M' and lines[i+2][j]=='A' and lines[i+3][j]=='S':
        tmp_res += 1 # DROITE
    if j >= length and lines[i][j-1]=='M' and lines[i][j-2]=='A' and lines[i][j-3]=='S':
        tmp_res += 1 # HAUT
    if j < len(lines[i]) - length and lines[i][j+1]=='M' and lines[i][j+2]=='A' and lines[i][j+3]=='S':
        tmp_res += 1 # BAS
    if i >= length and j >= length and lines[i-1][j-1]=='M' and lines[i-2][j-2]=='A' and lines[i-3][j-3]=='S':
        tmp_res += 1 # GAUCHE HAUT
    if i < len(lines) - length and j >= length and lines[i+1][j-1]=='M' and lines[i+2][j-2]=='A' and lines[i+3][j-3]=='S':
        tmp_res += 1 # DROITE HAUT
    if i >= length and j < len(lines[i]) - length and lines[i-1][j+1]=='M' and lines[i-2][j+2]=='A' and lines[i-3][j+3]=='S':
        tmp_res += 1 # GAUCHE BAS
    if i < len(lines) - length and j < len(lines[i]) - length and lines[i+1][j+1]=='M' and lines[i+2][j+2]=='A' and lines[i+3][j+3]=='S':
        tmp_res += 1 # DROITE BAS
    return tmp_res

res = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j]=='X':
            res += checkXmax(lines, i, j)

print("Part 1 : ", res)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))

solution2Start = time.time()
# Solution 2

res = 0
for i in range(1, len(lines)-1):
    for j in range(1, len(lines[i])-2):
        res += lines[i-1][j-1] + lines[i+1][j-1] + lines[i][j] + lines[i+1][j+1] + lines[i-1][j+1] in ('MSASM','SMAMS', 'MMASS', 'SSAMM')

print("Part 2 : ", res)

res = sum([sum([lines[i-1][j-1] + lines[i+1][j-1] + lines[i][j] + lines[i+1][j+1] + lines[i-1][j+1] in ('MSASM','SMAMS', 'MMASS', 'SSAMM') for j in range(1, len(lines[i])-2)]) for i in range(1, len(lines)-1)])

print("Part 2 one liner: ", res)
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))
