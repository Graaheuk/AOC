import time
import os
import sys

# Reading input
start = time.time()

file_path = os.path.dirname(sys.argv[0])
f = open('C:/Users/Graaheuk/Desktop/AOC/2024/2/input.dat','r')
lines = f.readlines()
end = time.time()
print("Time to read the file : " + str(end - start))
solutionStart = time.time()
# Solution 1
res = 0 

def isSafe(line):
    for i in range(len(line)-1):
        if abs(int(line[i]) - int(line[i+1])) not in [1,2,3]:
            return False
    return all(int(line[i]) < int(line[i + 1]) for i in range(len(line)-1)) or all(int(line[i]) > int(line[i + 1]) for i in range(len(line)-1))

for line in lines:
    tmp = line.split(" ")
    if isSafe(tmp):
        res += 1


print("Part 1 : ", res)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))

solution2Start = time.time()
# Solution 2
res = 0 

def isSafeWithOneError(line):
    for i in range(len(line)):
        if isSafe(line[:i] + line[i+1:]):
            return True
    return False

for line in lines:
    tmp = line.split(" ")
    if isSafe(tmp) or isSafeWithOneError(tmp):
        res += 1

print("Part 2 : ", res)

end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))
