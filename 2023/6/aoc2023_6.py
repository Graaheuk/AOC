import time
import os
import sys

# Reading input
start = time.time()

file_path = os.path.dirname(sys.argv[0])
f= open(file_path + '/input.dat','r')
lines = f.readlines()
end = time.time()
print("Time to read the file : " + str(end - start))
solutionStart = time.time()
# Solution 1

times = list(filter(None, lines[0].split(': ')[1].split(' ')))
times[-1] = times[-1].strip()
dist = list(filter(None, lines[1].split(': ')[1].split(' ')))

raceList = []
for t in times:
    distList = []
    for i in range(int(t)):
        distList += [i * (int(t) - i)]
    raceList += [distList]

racesScore = 1
for i in range(len(raceList)):
    raceScore = 0
    for distance in raceList[i]:
        if distance > int(dist[i]):
            raceScore += 1
    racesScore *= raceScore

print("Part 1 : ", racesScore)
end = time.time()
print("Solution 1 time : " + str(end - solutionStart))
solution2Start = time.time()
# Solution 2

t = ''.join(list(filter(None, lines[0].split(': ')[1].split(' '))))
t = t.strip()
dist = ''.join(list(filter(None, lines[1].split(': ')[1].split(' '))))

distanceList = []

for i in range(int(t)):
    distanceList += [i * (int(t) - i)]

raceScore = 0
for distance in distanceList:
    if distance > int(dist):
        raceScore += 1

print("Part 2 : ", raceScore)
end = time.time()
print("Solution 2 time : " + str(end - solution2Start))
print("Total time : " + str(end - start))