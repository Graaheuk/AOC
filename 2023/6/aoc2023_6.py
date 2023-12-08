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

times = list(filter(None, lines[0].split(': ')[1].split(' ')))
times[-1] = times[-1].strip()
dist = list(filter(None, lines[1].split(': ')[1].split(' ')))

def calculate(t, d):
    res = 0
    for x in range(t + 1):
        dx = x * (t - x)
        if dx >= d:
            res += 1
    return res

raceScore = 1
for i in range(len(times)):
    raceScore *= calculate(int(times[i]),int(dist[i]))

print("Part 1 : ", raceScore)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()
# Solution 2

t = int(''.join(list(filter(None, lines[0].split(': ')[1].split(' ')))).strip())
dist = int(''.join(list(filter(None, lines[1].split(': ')[1].split(' ')))))

delta = (t**2 - 4*dist) ** (1/2)
x1 = (t - delta) / 2
x2 = int(t + delta) / 2

if isinstance(x1, int): 
    x1 -= 1
else:
    x1 = int(x1)

raceScore = int(x2 - x1) 

print("Part 2 : ", raceScore)
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))