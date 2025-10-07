from operator import contains
import time
import os
import sys
import re

# Reading input
start = time.time()

file_path = os.path.dirname(sys.argv[0])
f = open('C:/Users/Graaheuk/Desktop/AOC/2024/3/input.dat','r')
lines = f.readlines()
end = time.time()
print("Time to read the file : " + str(end - start))
solutionStart = time.time()
# Solution 1
res = 0

find = []
r = re.compile(r"(mul\(){1}(\d+)(,{1})(\d+)\)")
for line in lines:
    find += r.findall(line)

for i in find:
    res += int(i[1]) * int(i[3])

print("Part 1 : ", res)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))

solution2Start = time.time()
# Solution 2
res = 0 

find = []
r = re.compile(r"(mul\(){1}(\d+)(,{1})(\d+)\)|(do\(\)){1}|(don't\(\)){1}")
for line in lines:
    find += r.findall(line)

state = True
for i in find:
    if "don't()" in i:
        state = False
    elif "do()" in i:
        state = True
    elif state:
        res += int(i[1]) * int(i[3])

print("Part 2 : ", res)

end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))
